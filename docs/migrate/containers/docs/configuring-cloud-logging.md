---
url: https://docs.cloud.google.com/migrate/containers/docs/configuring-cloud-logging/
title: Configure logging to Cloud Logging \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:03.357914+00:00
---

# Configure logging to Cloud Logging  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/configuring-cloud-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure logging to Cloud Logging

This document describes how to customize logging by using a `ConfigMap` on your target workload cluster.

## Available logs

By default, Migrate to Containers writes entries from the following sources:

  * Entries written to `stdout` of `init`, the parent of all Linux processes.
  * Contents from `/var/log/syslog`.



In Cloud Logging, entries from the supported log files will each appear on a line in the log in the following form. Labels are defined in a `ConfigMap` that lists log files.
    
    
    date time label log-output
    

The following example illustrates the form with an entry from MySQL:
    
    
    2019-09-22 12:43:08.681193976 +0000 UTC mysql log-output
    

You can opt to extend the log forwarding feature to propagate logs for other processes and applications running in the migrated container.

## Forward application logs to Cloud Logging

In order to log to Cloud Logging from applications on VMs migrated with Migrate to Containers, you must have the following in place:

  * Create a `ConfigMap` on your target workload cluster that specifies a list of the file system log files whose entries should be written to Cloud Logging.

You can use the sample `ConfigMap` included in the following section as a reference covering many common log files.

  * The `ConfigMap` must be in the same namespace as your container's `Deployment` or `StatefulSet`.

  * The `Deployment` or `StatefulSet` must reference `ConfigMap`.

  * If you're migrating to Google Distributed Cloud, install [Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect/overview) on your Google Distributed Cloud cluster. Connect is required to pass data back to Cloud Logging.



    
    
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          creationTimestamp: null
          labels:
            app: my-app
            migrate-for-anthos-type: workload
          name: test-ibsc-appenhmutimiy
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: test-ibsc-appenhmutimiy
              migrate-for-anthos-type: workload
          strategy: {}
          template:
            metadata:
              creationTimestamp: null
              labels:
                app: test-ibsc-appenhmutimiy
                migrate-for-anthos-type: workload
            spec:
              containers:
              - image: gcr.io/myproject/my-container-image:v1.0.0
                name: test-ibsc-appenhmutimiy
                readinessProbe:
                  exec:
                    command:
                    - /code/ready.sh
                resources: {}
                securityContext:
                  privileged: true
                volumeMounts:
                - mountPath: /sys/fs/cgroup
                  name: cgroups
                - mountPath: /code/config/logs/
                  name: logs-config
              volumes:
              - hostPath:
                  path: /sys/fs/cgroup
                  type: Directory
                name: cgroups
              - configMap:
                  name: <ConfigMap name>
                name: logs-config
    

## Use `ConfigMap` for common application logs

The reference `ConfigMap` YAML in the following section covers a list of common application log files and their application labels. You can copy the reference `ConfigMap` YAML as is, or modify it to remove entries or add your custom application logs.

To edit the list of log files, edit the elements following the `logs:` line. A log sub-element consists of the following structure:
    
    
    label:
      - path-with-simple-wildcards

For example:
    
    
    tomcat:
      - /var/log/tomcat*/catalina.out
      - /var/log/tomcat*/localhost.*.log
    

### Reference `ConfigMap` for common apps
    
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      creationTimestamp: null
      name: <ConfigMap name>
    data:
      logs.yaml: |
        logs:
          mysql:
          - /var/log/mysql.log
          - /var/log/mysql/mysql.log
          mongodb:
          - /var/log/mongodb/*.log
          memcached:
          - /var/log/memcached.log
          redis:
          - /var/log/redis*.log
          - /var/log/redis/*.log
          rabbitmq-startup:
          - /var/log/rabbitmq/startup_log
          rabbitmq-startup_err:
          - /var/log/rabbitmq/startup_err
          rabbitmq-sasl:
          - /var/log/rabbitmq/*-sasl.log
          sugarcrm:
          - /var/www/*/sugarcrm.log
          tomcat-localhost_access_log:
          - /var/log/tomcat*/localhost_access_log*.txt
          tomcat:
          - /var/log/tomcat*/catalina.out
          - /var/log/tomcat*/localhost.*.log
          apache-access:
          - /var/log/apache*/access.log
          - /var/log/apache*/access_log
          - /var/log/httpd/access.log
          - /var/log/httpd/access_log
          apache-error:
          - /var/log/apache*/error.log
          - /var/log/apache*/error_log
          - /var/log/httpd/error.log
          - /var/log/httpd/error_log
          cassandra:
          - /var/log/cassandra/system.log
          - /var/log/cassandra/cassandra.log
          - /var/log/cassandra/output.log
          chef-bookshelf:
          - /var/log/chef-server/bookshelf/current
          chef-expander:
          - /var/log/chef-server/chef-expander/current
          chef-pedant-http-traffic:
          - /var/log/chef-server/chef-pedant/http-traffic.log
          chef-server-webui:
          - /var/log/chef-server/chef-server-webui/current
          chef-solr:
          - /var/log/chef-server/chef-solr/current
          chef-erchef-current:
          - /var/log/chef-server/erchef/current
          chef-erchef:
          - /var/log/chef-server/erchef/erchef.log.1
          chef-nginx-access:
          - /var/log/chef-server/nginx/access.log
          chef-nginx-error:
          - /var/log/chef-server/nginx/error.log
          chef-nginx-rewrite-port-80:
          - /var/log/chef-server/nginx/rewrite-port-80.log
          chef-postgresql:
          - /var/log/chef-server/postgresql/current
          chef-rabbitmq:
          - /var/log/chef-server/rabbitmq/current
          postgresql:
          - /var/log/postgres*/*.log
          - /var/log/pgsql/*.log
          puppet-access:
          - /var/log/pe-httpd/access.log
          puppet-puppetmasteraccess:
          - /var/log/pe-httpd/puppetmasteraccess.log
          puppet-activemq:
          - /var/log/pe-activemq/activemq.log
          puppet-activemq-wrapper:
          - /var/log/pe-activemq/wrapper.log
          puppet-mcollective:
          - /var/log/pe-mcollective/mcollective.log
          puppet-mcollective-audit:
          - /var/log/pe-mcollective/mcollective_audit.log
          puppet-puppetdb:
          - /var/log/pe-puppetdb/pe-puppetdb.log
          puppet-dashboard-error:
          - /var/log/pe-httpd/puppetdashboard.error.log
          puppet-dashboard-mcollective-client:
          - /var/log/pe-puppet-dashboard/mcollective_client.log
          puppet-dashboard-production:
          - /var/log/pe-puppet-dashboard/production.log
          puppet-dashboard-event-inspector:
          - /var/log/pe-puppet-dashboard/event-inspector.log
          puppet-dashboard-certificate-manager:
          - /var/log/pe-puppet-dashboard/certificate_manager.log
          puppet-dashboard-live-management:
          - /var/log/pe-puppet-dashboard/live-management.log
          puppet-console-cas-client:
          - /var/log/pe-console-auth/cas_client.log
          puppet-console-auth-cas:
          - /var/log/pe-console-auth/cas.log
          puppet-console-auth:
          - /var/log/pe-console-auth/auth.log
          puppet-dashboard-access:
          - /var/log/pe-httpd/puppetdashboard.access.log
          puppet-dashboard-failed-reports:
          - /var/log/pe-puppet-dashboard/failed_reports.log
          puppet-error:
          - /var/log/pe-httpd/error.log
          puppet-other-vhosts-access:
          - /var/log/pe-httpd/other_vhosts_access.log
          puppet-masterhttp:
          - /var/log/pe-puppet/masterhttp.log
          - /var/log/puppet/masterhttp.log
          puppet-rails:
          - /var/log/pe-puppet/rails.log
          puppet-http:
          - /var/log/puppet/http.log
          gitlab-application:
          - /home/git/gitlab/log/application.log
          gitlab-production:
          - /home/git/gitlab/log/production.log
          gitlab-sidekiq:
          - /home/git/gitlab/log/sidekiq.log
          gitlab-unicorn-stdout:
          - /home/git/gitlab/log/unicorn.stdout.log
          gitlab-unicorn-stderr:
          - /home/git/gitlab/log/unicorn.stderr.log
          gitlab-githost:
          - /home/git/gitlab/log/githost.log
          gitlab-satellites:
          - /home/git/gitlab/log/satellites.log
          gitlab-shell:
          - /home/git/gitlab-shell/gitlab-shell.log
          jenkins:
          - /var/log/jenkins/jenkins.log
          jetty-request:
          - /var/log/jetty/*.request.log
          jetty-stderrout:
          - /var/log/jetty/*.stderrout.log
          jetty-out:
          - /var/log/jetty/out.log
          joomla:
          - /var/www/joomla/logs/*.log
          magento-system:
          - /var/www/magento/var/log/system.log
          magento-exception:
          - /var/www/magento/var/log/exception.log
          magento-report:
          - /var/www/magento/var/report/*
          mediawiki:
          - /var/log/mediawiki/*.log
          nginx-access:
          - /var/log/nginx/access.log
          nginx-error:
          - /var/log/nginx/error.log
          redmine:
          - /var/log/redmine/*.log
          salt-master:
          - /var/log/salt/master
          salt-minion:
          - /var/log/salt/minion
          salt-key:
          - /var/log/salt/key
          salt-syndic:
          - /var/log/salt/syndic.loc
          solr:
          - /var/log/solr/*.log
          sugarcrm:
          - /var/www/*/sugarcrm.log
          tomcat-localhost_access_log:
          - /var/log/tomcat*/localhost_access_log.*.txt
          tomcat:
          - /var/log/tomcat*/catalina.out,/var/log/tomcat*/localhost.*.log
    

## What's next

  * Learn how to [mount external volumes](https://docs.cloud.google.com/migrate/containers/docs/mounting-external-volumes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
