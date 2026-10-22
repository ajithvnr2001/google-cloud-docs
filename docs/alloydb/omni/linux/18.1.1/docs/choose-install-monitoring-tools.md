---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/choose-install-monitoring-tools/
title: Use AlloyDB Omni monitoring tools \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:38:32.013524+00:00
---

# Use AlloyDB Omni monitoring tools  |  AlloyDB Omni using RPM: 18.1.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/choose-install-monitoring-tools/

This page documents AlloyDB Omni version **18.1.1** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/overview)



Send feedback 

#  Use AlloyDB Omni monitoring tools Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.1keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/choose-install-monitoring-tools)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/choose-install-monitoring-tools)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/choose-install-monitoring-tools)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/choose-install-monitoring-tools)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/choose-install-monitoring-tools)

This page lists the tools you can use to monitor your AlloyDB Omni instance. 

## Monitoring tools

The following table lists the tools you can choose and install to monitor your AlloyDB Omni instance:

To | Use | Description  
---|---|---  
Monitor performance and availability | [Datadog](https://www.datadoghq.com/) | Monitor the performance, availability, and health of your AlloyDB Omni instance.  
Export observability data from your instance | [Postgres Exporter](https://github.com/prometheus-community/postgres_exporter/) | Export the results of observability queries. [To install Postgres Exporter](https://github.com/prometheus-community/postgres_exporter/blob/master/README.md)  
Retrieve observability data in a readable format | [Prometheus](https://prometheus.io/) | Monitoring system to return the observability data in a readable format. To install Prometheus  
Display data in a dashboard | [Grafana](https://grafana.com/) | Create a dashboard to display metrics. To install Grafana  
Retrieve performance data for analysis | [Performance snapshot reports](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/optimize-database-performance-compare-snapshots) | Retrieve performance data to identify the cause of performance issues.  
Monitor your instance | [Built-in AlloyDB Omni monitoring tool](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/manage) | Monitor your instance by using the built-in monitoring tool to fetch and analyze  
  
AlloyDB Omni metrics.

## Install Postgres Exporter

Postgres Exporter is a tool that exports observability queries in a format that Prometheus, a monitoring system, can read. The exporter comes with many standard queries built in it and you can add additional queries and rules depending on your needs. Additional security options, such as SSL and user authentication, can be configured as well. For this example, only the basic configuration options are used.

### Install

  1. Create a directory for Postgres Exporter.
         
         sudo mkdir /opt/postgres_exporter
         sudo chown USER_ACCOUNT:USER_ACCOUNT /opt/postgres_exporter
         cd /opt/postgres_exporter

  2. Download Postgres Exporter.
         
         wget https://github.com/prometheus-community/postgres_exporter/releases/download/v0.15.0/postgres_exporter-0.15.0.linux-amd64.tar.gz
         

  3. Extract Postgres Exporter.
         
         tar -xzvf postgres_exporter-0.15.0.linux-amd64.tar.gz
         

  4. Copy Postgres Exporter to the directory you created.
         
         cd postgres_exporter-0.15.0.linux-amd64
         sudo cp postgres_exporter /usr/local/bin

  5. Create an appropriate `.env` file for Postgres Exporter.
         
         cd /opt/postgres_exporter
         sudo vi postgres_exporter.env

  6. Add data sources to `/opt/postgres_exporter/postgres_exporter.env` to monitor one or more databases.

To monitor a single database, add the following line:
         
         DATA_SOURCE_NAME="postgresql://USERNAME:PASSWORD@POSTGRES_IP_ADDRESS:PORT/DATABASE_NAME?sslmode=disable"
         

To monitor all databases, add the following line:
         
         DATA_SOURCE_NAME="postgresql://USERNAME:PASSWORD@POSTGRES_IP_ADDRESS:PORT/?sslmode=disable"
         

Replace the following variables:

     * `USERNAME`: Username to sign in to the database.
     * `PASSWORD`: Password for the user account.
     * `POSTGRES_IP_ADDRESS`: IP address of the AlloyDB Omni instance.
     * `PORT`: Port the database is hosted on.
     * `DATABASE_NAME`: Name of the database.
  7. Add the following information to `/etc/systemd/system/postgres_exporter.service` so Postgres Exporter survives reboots.
         
         [Unit]
         Description=Prometheus exporter for Postgresql
         Wants=network-online.target
         After=network-online.target
         [Service]
         User=postgres
         Group=postgres
         WorkingDirectory=/opt/postgres_exporter
         EnvironmentFile=/opt/postgres_exporter/postgres_exporter.env
         ExecStart=/usr/local/bin/postgres_exporter --web.listen-address=:POSTGRES_EXPORTER_PORT --web.telemetry-path=/metrics
         Restart=always
         [Install]
         WantedBy=multi-user.target
         

Replace the following variable:

     * `POSTGRES_EXPORTER_PORT`: Port Postgres Exporter is hosted on. We recommend using port `9187`.
  8. Reload Postgres Exporter.
         
         sudo systemctl daemon-reload
         

  9. Start Postgres Exporter.
         
         sudo systemctl start postgres_exporter
         sudo systemctl enable postgres_exporter
         sudo systemctl status postgres_exporter




Postgres Exporter should now be available at the following URL:
    
    
    http://POSTGRES_EXPORTER_HOST_IP_ADDRESS:POSTGRES_EXPORTER_PORT/metrics
    

Replace the following variables:

  * `POSTGRES_EXPORTER_HOST_IP_ADDRESS`: IP address of your machine.
  * `POSTGRES_EXPORTER_PORT`: Port you used in step 7.



## Prometheus

Prometheus is a monitoring system that can be used to query Postgres Exporter and return the observability data in a readable format.

### Install

  1. Create a `prometheus` user.
         
         sudo groupadd --system prometheus
         sudo useradd -s /sbin/nologin --system -g prometheus prometheus

  2. Create directories for Prometheus.
         
         sudo mkdir /etc/prometheus
         sudo mkdir /var/lib/prometheus

  3. Download Prometheus.
         
         wget https://github.com/prometheus/prometheus/releases/download/v2.52.0/prometheus-2.52.0.linux-amd64.tar.gz
         

  4. Extract Prometheus.
         
         sudo tar xvf prometheus*.tar.gz
         cd prometheus*/
         sudo mv prometheus /usr/local/bin
         sudo mv promtool /usr/local/bin

  5. Set ownership of Prometheus to the `prometheus` user.
         
         sudo chown prometheus:prometheus /usr/local/bin/prometheus
         sudo chown prometheus:prometheus /usr/local/bin/promtool

  6. Move the configuration files to the correct location.
         
         sudo mv consoles /etc/prometheus
         sudo mv console_libraries /etc/prometheus
         sudo mv prometheus.yml /etc/prometheus

  7. Set ownership of the Prometheus directories to the `prometheus` user.
         
         sudo chown prometheus:prometheus /etc/prometheus
         sudo chown prometheus:prometheus /etc/prometheus/*
         sudo chown -R prometheus:prometheus /etc/prometheus/consoles
         sudo chown -R prometheus:prometheus /etc/prometheus/console_libraries
         sudo chown -R prometheus:prometheus /var/lib/prometheus

  8. Add the following information to `/etc/prometheus/prometheus.yml` so that Prometheus can query Postgres Exporter.
         
         global:
           scrape_interval: 15s
         
         scrape_configs:
         - job_name: postgres
           static_configs:
           - targets: ['POSTGRES_EXPORTER_MACHINE_IP_ADDRESS:9187']
         

  9. Add the following information to `/etc/systemd/system/prometheus.service` so Prometheus survives reboots.
         
         [Unit]
         Description=Prometheus
         Wants=network-online.target
         After=network-online.target
         
         [Service]
         User=prometheus
         Group=prometheus
         Type=simple
         ExecStart=/usr/local/bin/prometheus \
             --config.file /etc/prometheus/prometheus.yml \
             --storage.tsdb.path /var/lib/prometheus/ \
             --web.console.templates=/etc/prometheus/consoles \
             --web.console.libraries=/etc/prometheus/console_libraries
         
         [Install]
         WantedBy=multi-user.target
         

  10. Reload systemd manager configuration.
         
         sudo systemctl daemon-reload
         

  11. Start Prometheus.
         
         sudo systemctl start prometheus
         sudo systemctl enable prometheus
         sudo systemctl status prometheus




Prometheus should now be available at the following URL:
    
    
    http://PROMETHEUS_HOST_IP_ADDRESS:9090
    

Replace the following variable:

  * `PROMETHEUS_HOST_IP_ADDRESS`: IP address of your machine.



## Grafana

Grafana is a dashboarding tool that exposes Prometheus metrics to an end user through a dashboard. Multiple standard dashboards are available for Postgres Exporter and this observability example leverages those available dashboards. Grafana is available through normal `apt` and `yum` repositories and we use those to install this product.

### Install

  1. Install Grafana.

For Ubuntu and Debian systems, run the following commands:
         
         sudo apt-get update
         sudo apt-get install grafana

For RHEL, CentOS, or Rocky Linux systems, complete the following tasks:

     1. Import the GPG key.
            
            wget -q -O gpg.key https://rpm.grafana.com/gpg.key
            sudo rpm --import gpg.key

     2. Create the `/etc/yum.repos.d/grafana.repo` file with the following content:
            
            [grafana]
            name=grafana
            baseurl=https://rpm.grafana.com
            repo_gpgcheck=1
            enabled=1
            gpgcheck=1
            gpgkey=https://rpm.grafana.com/gpg.key
            sslverify=1
            sslcacert=/etc/pki/tls/certs/ca-bundle.crt
            

     3. Install Grafana.
            
            sudo dnf install grafana
            

  2. Reload Grafana.
         
         sudo systemctl daemon-reload
         

  3. Start Grafana.
         
         sudo systemctl start grafana-server
         sudo systemctl enable grafana-server
         sudo systemctl status grafana-server




Grafana should now be available at the following URL:
    
    
    http://GRAFANA_HOST_IP_ADDRESS:3000
    

Replace the following variable:

  * `GRAFANA_HOST_IP_ADDRESS`: IP address of your machine.



### Load a dashboard

You can find general instructions on how to configure and operate Grafana on [Set up Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/). There are many public dashboards available, but we recommend the following [PostgreSQL statistics dashboard](https://grafana.com/grafana/dashboards/13494-postgresql-statistics/).

To load a dashboard, complete the following tasks:

  1. Set up Grafana.

     1. Open the Grafana console using the URL address from Grafana's Install section. The default username and password is `admin`.

     2. Change the default password.

     3. If the Prometheus data source is not added, navigate to **Home** > **Data sources**.

     4. Click **Add new data source**.

     5. Select **Prometheus**.

     6. In the **Prometheus server URL** field, enter the URL address from Prometheus' Install section.

     7. Change the following configuration settings:

        * **Prometheus type** : Select **Prometheus**.
        * **Prometheus version** : Select **> 2.5.x**.
     8. Click **Save & test**.

  2. Create a new dashboard.

     1. Navigate to **Home** > **Dashboards**.

     2. Click **New**.

     3. Select **New dashboard**.

     4. Click **Import dashboard**.

     5. Enter the following URL: https://grafana.com/grafana/dashboards/13494-postgresql-statistics/.

     6. Click **Load**.

     7. Change the **Name** of the dashboard to `PRODUCT_NAME PostgreSQL statistics`.

Replace `PRODUCT_NAME` with the name of your product.

     8. Select your data source from the **Prometheus** field.

     9. Click **Import**.




## Performance snapshot reports

Performance snapshot reports are a built-in AlloyDB Omni tool that captures and analyzes performance data to help you identify the cause of performance issues. This tool complements other AlloyDB Omni observability features like [systems insights](https://docs.cloud.google.com/alloydb/docs/monitor-instance), [query insights](https://docs.cloud.google.com/alloydb/docs/query-insights-overview), and the [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer), which provide real-time metrics about your instance.

For more information, see [Optimize database performance by comparing performance snapshots](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/optimize-database-performance-compare-snapshots).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
