---
url: https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-gce/
title: Connect to a Redis instance from a Compute Engine VM \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:38.059913+00:00
---

# Connect to a Redis instance from a Compute Engine VM  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-gce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Connect to a Redis instance from a Compute Engine VM Stay organized with collections  Save and categorize content based on your preferences. 

You can connect to your Redis instance from Compute Engine VM instances that use the same authorized network as your Redis instance.

## Setup

If you have already installed the Google Cloud CLI, created a Redis instance, and created a Cloud Storage bucket you can skip these steps.

  1. [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs) and initialize:
         
         gcloud init
         

  2. Follow the [Quickstart Guide](https://docs.cloud.google.com/memorystore/docs/redis/create-instance-gcloud) to create a Redis instance. Take note of the zone, IP address, and port of the Redis instance.

  3. Create a Cloud Storage bucket where the application artifact for this sample application will be uploaded. For more, see [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).




## Configuring the gcloud settings for the sample application

  1. Set the `gcloud` default project to your sample app project. 
         
         gcloud config set project [PROJECT_ID]




## Sample application

This sample HTTP server application establishes a connection to a Redis instance from a Compute Engine VM instance.

Clone the repository for your chosen programming language and navigate to the folder that contains the sample code:

### Go
    
    
    git clone https://github.com/GoogleCloudPlatform/golang-samples
    cd golang-samples/memorystore/redis
    

### Java
    
    
    git clone https://github.com/GoogleCloudPlatform/java-docs-samples
    cd java-docs-samples/memorystore/redis
    

### Node.js
    
    
    git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples
    cd nodejs-docs-samples/memorystore/redis
    

### Python
    
    
    git clone https://github.com/GoogleCloudPlatform/python-docs-samples
    cd python-docs-samples/memorystore/redis
    

This sample application increments a Redis counter every time the `/` endpoint is accessed.

### Go

This application uses the [`github.com/gomodule/redigo/redis`](https://godoc.org/github.com/gomodule/redigo/redis) client. Install it by running the following command:
    
    
    go get github.com/gomodule/redigo/redis@latest
    

Example application:
    
    
    // Package main is a basic app that connects to a managed Redis instance.
    package main
    
    import (
    	"fmt"
    	"log"
    	"net/http"
    	"os"
    
    	"github.com/gomodule/redigo/redis"
    )
    
    var redisPool *redis.Pool
    
    func incrementHandler(w http.ResponseWriter, r *http.Request) {
    	conn := redisPool.Get()
    	defer conn.Close()
    
    	counter, err := redis.Int(conn.Do("INCR", "visits"))
    	if err != nil {
    		http.Error(w, "Error incrementing visitor counter", http.StatusInternalServerError)
    		return
    	}
    	fmt.Fprintf(w, "Visitor number: %d", counter)
    }
    
    func main() {
    	redisHost := os.Getenv("REDISHOST")
    	redisPort := os.Getenv("REDISPORT")
    	redisAddr := fmt.Sprintf("%s:%s", redisHost, redisPort)
    
    	const maxConnections = 10
    	redisPool = &redis.Pool{
    		MaxIdle: maxConnections,
    		Dial:    func() (redis.Conn, error) { return redis.Dial("tcp", redisAddr) },
    	}
    
    	http.HandleFunc("/", incrementHandler)
    
    	port := os.Getenv("PORT")
    	if port == "" {
    		port = "8080"
    	}
    	log.Printf("Listening on port %s", port)
    	if err := http.ListenAndServe(":"+port, nil); err != nil {
    		log.Fatal(err)
    	}
    }
    

### Java

This application is Jetty 3.1 servlet-based.

It uses the [Jedis](https://github.com/xetorthio/jedis) library:
    
    
    <dependency>
      <groupId>redis.clients</groupId>
      <artifactId>jedis</artifactId>
      <version>5.1.0</version>
    </dependency>

The `AppServletContextListener` class is used to create a long-lived Redis connection pool:
    
    
    package com.example.redis;
    
    import java.io.IOException;
    import java.util.Properties;
    import javax.servlet.ServletContextEvent;
    import javax.servlet.ServletContextListener;
    import javax.servlet.annotation.WebListener;
    import redis.clients.jedis.JedisPool;
    import redis.clients.jedis.JedisPoolConfig;
    
    @WebListener
    public class AppServletContextListener implements ServletContextListener {
    
      private Properties config = new Properties();
    
      private JedisPool createJedisPool() throws IOException {
        String host;
        Integer port;
        config.load(
            Thread.currentThread()
                .getContextClassLoader()
                .getResourceAsStream("application.properties"));
        host = config.getProperty("redis.host");
        port = Integer.valueOf(config.getProperty("redis.port", "6379"));
    
        JedisPoolConfig poolConfig = new JedisPoolConfig();
        // Default : 8, consider how many concurrent connections into Redis you will need under load
        poolConfig.setMaxTotal(128);
    
        return new JedisPool(poolConfig, host, port);
      }
    
      @Override
      public void contextDestroyed(ServletContextEvent event) {
        JedisPool jedisPool = (JedisPool) event.getServletContext().getAttribute("jedisPool");
        if (jedisPool != null) {
          jedisPool.destroy();
          event.getServletContext().setAttribute("jedisPool", null);
        }
      }
    
      // Run this before web application is started
      @Override
      public void contextInitialized(ServletContextEvent event) {
        JedisPool jedisPool = (JedisPool) event.getServletContext().getAttribute("jedisPool");
        if (jedisPool == null) {
          try {
            jedisPool = createJedisPool();
            event.getServletContext().setAttribute("jedisPool", jedisPool);
          } catch (IOException e) {
            // handle exception
          }
        }
      }
    }

The `VisitCounterServlet` class is a web servlet that increments a Redis counter:
    
    
    package com.example.redis;
    
    import java.io.IOException;
    import java.net.SocketException;
    import javax.servlet.annotation.WebServlet;
    import javax.servlet.http.HttpServlet;
    import javax.servlet.http.HttpServletRequest;
    import javax.servlet.http.HttpServletResponse;
    import redis.clients.jedis.Jedis;
    import redis.clients.jedis.JedisPool;
    
    @WebServlet(name = "Track visits", value = "")
    public class VisitCounterServlet extends HttpServlet {
    
      @Override
      public void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        try {
          JedisPool jedisPool = (JedisPool) req.getServletContext().getAttribute("jedisPool");
    
          if (jedisPool == null) {
            throw new SocketException("Error connecting to Jedis pool");
          }
          Long visits;
    
          try (Jedis jedis = jedisPool.getResource()) {
            visits = jedis.incr("visits");
          }
    
          resp.setStatus(HttpServletResponse.SC_OK);
          resp.getWriter().println("Visitor counter: " + String.valueOf(visits));
        } catch (Exception e) {
          resp.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, e.getMessage());
        }
      }
    }

### Node.js

This application uses the [`redis`](https://www.npmjs.com/package/redis) module. This is a sample `package.json` file:
    
    
    {
      "name": "memorystore-redis",
      "description": "An example of using Memorystore(Redis) with Node.js",
      "version": "0.0.1",
      "private": true,
      "license": "Apache Version 2.0",
      "author": "Google Inc.",
      "engines": {
        "node": ">=20.0.0"
      },
      "dependencies": {
        "redis": "^4.0.0"
      }
    }
    
    

Sample application code:
    
    
    'use strict';
    const http = require('http');
    const redis = require('redis');
    
    const REDISHOST = process.env.REDISHOST || 'localhost';
    const REDISPORT = process.env.REDISPORT || 6379;
    
    const client = redis.createClient({
      url: `redis://${REDISHOST}:${REDISPORT}`,
    });
    
    client.on('error', err => console.error('ERR:REDIS:', err));
    
    client
      .connect()
      .then(() => {
        console.log('Connected to Redis');
        http
          .createServer(async (req, res) => {
            try {
              const reply = await client.incr('visits');
              res.writeHead(200, {'Content-Type': 'text/plain'});
              res.end(`Visitor number: ${reply}\n`);
            } catch (err) {
              console.error(err);
              res.statusCode = 500;
              res.end(err.message);
            }
          })
          .listen(8080, () => {
            console.log('Server listening on port 8080');
          });
      })
      .catch(err => {
        console.error('Failed to connect to Redis:', err);
        throw err;
      });

### Python

This application uses [Flask](https://flask.palletsprojects.com/en/1.1.x/) for web serving and the [`redis-py`](https://redis-py.readthedocs.io/en/latest/) package to communicate with the Redis instance.
    
    
    Flask==3.1.3; python_version >= '3.9'
    gunicorn==23.0.0
    redis==6.0.0
    Werkzeug==3.1.9; python_version >= '3.10'

Sample application code:
    
    
    import logging
    import os
    
    from flask import Flask
    import redis
    
    app = Flask(__name__)
    
    redis_host = os.environ.get("REDISHOST", "localhost")
    redis_port = int(os.environ.get("REDISPORT", 6379))
    redis_client = redis.StrictRedis(host=redis_host, port=redis_port)
    
    
    @app.route("/")
    def index():
        value = redis_client.incr("counter", 1)
        return f"Visitor number: {value}"
    
    
    @app.errorhandler(500)
    def server_error(e):
        logging.exception("An error occurred during a request.")
        return (
            """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(
                e
            ),
            500,
        )
    
    
    if __name__ == "__main__":
        # This is used when running locally. Gunicorn is used to run the
        # application on Google App Engine and Cloud Run.
        # See entrypoint in app.yaml or Dockerfile.
        app.run(host="127.0.0.1", port=8080, debug=True)

## Deploying the application to a Compute Engine VM

Navigate to the `gce_deployment` directory:
    
    
    cd gce_deployment
    

The deployment script uploads the artifact to the Cloud Storage path. It then launches a Compute Engine instance, creating a firewall to expose the port 8080. Then the startup script prepares the instance.

Set the `REDISHOST` and `REDISPORT` environmental variables:
    
    
       export REDISHOST=[REDISHOST]
       export REDISPORT=[REDISPORT]
    

where:

  * `REDISHOST` is the managed Redis instance IP.
  * `REDISPORT` is the managed Redis instance port by default 6379.



Set the `GCS_BUCKET_NAME` environmental variable:
    
    
         export GCS_BUCKET_NAME=[BUCKET_NAME]/[PATH]

where:

  * `BUCKET_NAME` is the name of your Cloud Storage bucket.
  * `PATH` is an optional path for the directory where you want to store the application artifact.



Here is a sample deployment script that deploys this application on a new Compute Engine VM instance.

### Go
    
    
    if [ -z "$REDISHOST" ]; then
      echo "Must set \$REDISHOST. For example: REDISHOST=127.0.0.1"
      exit 1
    fi
    
    if [ -z "$REDISPORT" ]; then
      echo "Must set \$REDISPORT. For example: REDISPORT=6379"
      exit 1
    fi
    
    if [ -z "$GCS_BUCKET_NAME" ]; then
      echo "Must set \$GCS_BUCKET_NAME. For example: GCS_BUCKET_NAME=my-bucket"
      exit 1
    fi
    
    if [ -z "$ZONE" ]; then
      ZONE=$(gcloud config get-value compute/zone -q)
      echo "$ZONE"
    fi
    
    
    # Cross compile the app for linux/amd64
    GOOS=linux GOARCH=amd64 go build -v -o app ../main.go
    # Add the app binary
    tar -cvf app.tar app
    # Copy to GCS bucket
    gcloud storage cp app.tar gs://"$GCS_BUCKET_NAME"/gce/
    
    # Create an instance
    gcloud compute instances create my-instance \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --machine-type=e2-small \
        --scopes cloud-platform \
        --metadata-from-file startup-script=startup-script.sh \
        --metadata gcs-bucket="$GCS_BUCKET_NAME",redis-host="$REDISHOST",redis-port="$REDISPORT" \
        --zone "$ZONE" \
        --tags http-server
    
    gcloud compute firewall-rules create allow-http-server-8080 \
        --allow tcp:8080 \
        --source-ranges 0.0.0.0/0 \
        --target-tags http-server \
        --description "Allow port 8080 access to http-server"

### Java
    
    
    if [ -z "$GCS_BUCKET_NAME" ]; then
        echo "Must set \$GCS_BUCKET_NAME. For example: GCS_BUCKET_NAME=my-bucket"
        exit 1
    fi
    
    if [ -z "$ZONE" ]; then
      ZONE=$(gcloud config get-value compute/zone -q)
      echo $ZONE
    fi
    
    if [ -z "$WAR" ]; then
      WAR=visitcounter-1.0-SNAPSHOT.war
    fi
    
    #Build the WAR package
    cd ..
    mvn clean package
    
    #Copy the WAR artifact to the GCS bucket location
    gcloud storage cp --recursive target/${WAR} gs://"$GCS_BUCKET_NAME"/gce/
    
    cd gce_deployment
    
    # Create an instance
    gcloud compute instances create my-instance \
        --image-family=debian-9 \
        --image-project=debian-cloud \
        --machine-type=g1-small \
        --scopes cloud-platform \
        --metadata-from-file startup-script=startup-script.sh \
        --metadata gcs-bucket=$GCS_BUCKET_NAME,app-war=$WAR \
        --zone $ZONE \
        --tags http-server
    
    gcloud compute firewall-rules create allow-http-server-8080 \
        --allow tcp:8080 \
        --source-ranges 0.0.0.0/0 \
        --target-tags http-server \
        --description "Allow port 8080 access to http-server"

### Node.js
    
    
    if [ -z "$REDISHOST" ]; then
      echo "Must set \$REDISHOST. For example: REDISHOST=127.0.0.1"
      exit 1
    fi
    
    if [ -z "$REDISPORT" ]; then
      echo "Must set \$REDISPORT. For example: REDISPORT=6379"
      exit 1
    fi
    
    if [ -z "$GCS_BUCKET_NAME" ]; then
      echo "Must set \$GCS_BUCKET_NAME. For example: GCS_BUCKET_NAME=my-bucket"
      exit 1
    fi
    
    if [ -z "$ZONE" ]; then
      ZONE=$(gcloud config get-value compute/zone -q)
      echo $ZONE
    fi
    
    #Upload the tar to GCS
    tar -cvf app.tar -C .. package.json server.js
    gcloud storage cp app.tar gs://"$GCS_BUCKET_NAME"/gce/
    
    # Create an instance
    gcloud compute instances create my-instance \
        --image-family=debian-9 \
        --image-project=debian-cloud \
        --machine-type=g1-small \
        --scopes cloud-platform \
        --metadata-from-file startup-script=startup-script.sh \
        --metadata gcs-bucket=$GCS_BUCKET_NAME,redis-host=$REDISHOST,redis-port=$REDISPORT \
        --zone $ZONE \
        --tags http-server
    
    gcloud compute firewall-rules create allow-http-server-8080 \
        --allow tcp:8080 \
        --source-ranges 0.0.0.0/0 \
        --target-tags http-server \
        --description "Allow port 8080 access to http-server"

### Python
    
    
    if [ -z "$REDISHOST" ]; then
      echo "Must set \$REDISHOST. For example: REDISHOST=127.0.0.1"
      exit 1
    fi
    
    if [ -z "$REDISPORT" ]; then
      echo "Must set \$REDISPORT. For example: REDISPORT=6379"
      exit 1
    fi
    
    if [ -z "$GCS_BUCKET_NAME" ]; then
      echo "Must set \$GCS_BUCKET_NAME. For example: GCS_BUCKET_NAME=my-bucket"
      exit 1
    fi
    
    if [ -z "$ZONE" ]; then
      ZONE=$(gcloud config get-value compute/zone -q)
      echo $ZONE
    fi
    
    #Upload the tar to GCS
    tar -cvf app.tar -C .. requirements.txt main.py
    # Copy to GCS bucket
    gcloud storage cp app.tar gs://"$GCS_BUCKET_NAME"/gce/
    
    # Create an instance
    gcloud compute instances create my-instance \
        --image-family=debian-13 \
        --image-project=debian-cloud \
        --machine-type=g1-small \
        --scopes cloud-platform \
        --metadata-from-file startup-script=startup-script.sh \
        --metadata gcs-bucket=$GCS_BUCKET_NAME,redis-host=$REDISHOST,redis-port=$REDISPORT \
        --zone $ZONE \
        --tags http-server
    
    gcloud compute firewall-rules create allow-http-server-8080 \
        --allow tcp:8080 \
        --source-ranges 0.0.0.0/0 \
        --target-tags http-server \
        --description "Allow port 8080 access to http-server"

Run the deployment script:
    
    
         chmod +x deploy.sh
         ./deploy.sh
    

### Application startup script

This startup script is used in the sample deployment script to prepare the instance. For more information about start up scripts and viewing startup script execution logs, see [Running Startup Scripts](https://docs.cloud.google.com/compute/docs/startupscript).

### Go
    
    
    set -ex
    
    # Talk to the metadata server to get the project id and location of application binary.
    PROJECTID=$(curl -s "http://metadata.google.internal/computeMetadata/v1/project/project-id" -H "Metadata-Flavor: Google")
    export PROJECTID
    GCS_BUCKET_NAME=$(curl -s "http://metadata.google.internal/computeMetadata/v1/instance/attributes/gcs-bucket" -H "Metadata-Flavor: Google")
    REDISHOST=$(curl -s "http://metadata.google.internal/computeMetadata/v1/instance/attributes/redis-host" -H "Metadata-Flavor: Google")
    REDISPORT=$(curl -s "http://metadata.google.internal/computeMetadata/v1/instance/attributes/redis-port" -H "Metadata-Flavor: Google")
    
    # Install dependencies from apt
    apt-get update
    apt-get install -yq ca-certificates supervisor
    
    # Install logging monitor. The monitor will automatically pickup logs send to
    # syslog.
    curl "https://storage.googleapis.com/signals-agents/logging/google-fluentd-install.sh" --output google-fluentd-install.sh
    checksum=$(sha256sum google-fluentd-install.sh | awk '{print $1;}')
    if [ "$checksum" != "ec78e9067f45f6653a6749cf922dbc9d79f80027d098c90da02f71532b5cc967" ]; then
        echo "Checksum does not match"
        exit 1
    fi
    chmod +x google-fluentd-install.sh && ./google-fluentd-install.sh
    service google-fluentd restart &
    
    gcloud storage cp gs://"$GCS_BUCKET_NAME"/gce/app.tar /app.tar
    mkdir -p /app
    tar -x -f /app.tar -C /app
    chmod +x /app/app
    
    # Create a goapp user. The application will run as this user.
    getent passwd goapp || useradd -m -d /home/goapp goapp
    chown -R goapp:goapp /app
    
    # Configure supervisor to run the Go app.
    cat >/etc/supervisor/conf.d/goapp.conf << EOF
    [program:goapp]
    directory=/app
    environment=HOME="/home/goapp",USER="goapp",REDISHOST=$REDISHOST,REDISPORT=$REDISPORT
    command=/app/app
    autostart=true
    autorestart=true
    user=goapp
    stdout_logfile=syslog
    stderr_logfile=syslog
    EOF
    
    supervisorctl reread
    supervisorctl update

### Java
    
    
    set -ex
    
    # Talk to the metadata server to get the project id and location of application binary.
    PROJECTID=$(curl -s "http://metadata.google.internal/computeMetadata/v1/project/project-id" -H "Metadata-Flavor: Google")
    GCS_BUCKET_NAME=$(curl -s "http://metadata.google.internal/computeMetadata/v1/instance/attributes/gcs-bucket" -H "Metadata-Flavor: Google")
    WAR=$(curl -s "http://metadata.google.internal/computeMetadata/v1/instance/attributes/app-war" -H "Metadata-Flavor: Google")
    
    gcloud storage cp gs://"$GCS_BUCKET_NAME"/gce/"$WAR" .
    
    # Install dependencies from apt
    apt-get update
    apt-get install -qq openjdk-8-jdk-headless
    
    # Make Java8 the default
    update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
    
    # Jetty Setup
    mkdir -p /opt/jetty/temp
    mkdir -p /var/log/jetty
    
    # Get Jetty
    curl -L https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-distribution/9.4.10.v20180503/jetty-distribution-9.4.10.v20180503.tar.gz -o jetty9.tgz
    tar xf jetty9.tgz  --strip-components=1 -C /opt/jetty
    
    # Add a Jetty User
    useradd --user-group --shell /bin/false --home-dir /opt/jetty/temp jetty
    
    cd /opt/jetty
    # Add running as "jetty"
    java -jar /opt/jetty/start.jar --add-to-startd=setuid
    cd /
    
    # very important - by renaming the war to root.war, it will run as the root servlet.
    mv $WAR /opt/jetty/webapps/root.war
    
    # Make sure "jetty" owns everything.
    chown --recursive jetty /opt/jetty
    
    # Configure the default paths for the Jetty service
    cp /opt/jetty/bin/jetty.sh /etc/init.d/jetty
    echo "JETTY_HOME=/opt/jetty" > /etc/default/jetty
    {
      echo "JETTY_BASE=/opt/jetty"
      echo "TMPDIR=/opt/jetty/temp"
      echo "JAVA_OPTIONS=-Djetty.http.port=8080"
      echo "JETTY_LOGS=/var/log/jetty"
    } >> /etc/default/jetty
    
    
    # Reload daemon to pick up new service
    systemctl daemon-reload
    
    # Install logging monitor. The monitor will automatically pickup logs sent to syslog.
    curl -s "https://storage.googleapis.com/signals-agents/logging/google-fluentd-install.sh" | bash
    service google-fluentd restart &
    
    service jetty start
    service jetty check
    
    echo "Startup Complete"

### Node.js
    
    
    set -ex
    
    # Talk to the metadata server to get the project id and location of application binary.
    PROJECTID=$(curl -s "http://metadata.google.internal/computeMetadata/v1/project/project-id" -H "Metadata-Flavor: Google")
    GCS_BUCKET_NAME=$(curl -s "http://metadata.google.internal/computeMetadata/v1/instance/attributes/gcs-bucket" -H "Metadata-Flavor: Google")
    REDISHOST=$(curl -s "http://metadata.google.internal/computeMetadata/v1/instance/attributes/redis-host" -H "Metadata-Flavor: Google")
    REDISPORT=$(curl -s "http://metadata.google.internal/computeMetadata/v1/instance/attributes/redis-port" -H "Metadata-Flavor: Google")
    
    # Install dependencies from apt
    apt-get update
    # Install Node.js 9
    curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
    apt-get install -yq ca-certificates supervisor nodejs build-essential
    
    
    # Install logging monitor. The monitor will automatically pickup logs send to
    # syslog.
    curl -s "https://storage.googleapis.com/signals-agents/logging/google-fluentd-install.sh" | bash
    service google-fluentd restart &
    
    gcloud storage cp gs://"$GCS_BUCKET_NAME"/gce/app.tar /app.tar
    mkdir -p /app
    tar -x -f /app.tar -C /app
    cd /app
    # Install the app dependencies
    npm install
    
    # Create a nodeapp user. The application will run as this user.
    getent passwd nodeapp || useradd -m -d /home/nodeapp nodeapp
    chown -R nodeapp:nodeapp /app
    
    # Configure supervisor to run the Go app.
    cat >/etc/supervisor/conf.d/nodeapp.conf << EOF
    [program:nodeapp]
    directory=/app
    environment=HOME="/home/nodeapp",USER="nodeapp",REDISHOST=$REDISHOST,REDISPORT=$REDISPORT
    command=node server.js
    autostart=true
    autorestart=true
    user=nodeapp
    stdout_logfile=syslog
    stderr_logfile=syslog
    EOF
    
    supervisorctl reread
    supervisorctl update

### Python
    
    
    set -v
    
    # Talk to the metadata server to get the project id and location of application binary.
    PROJECTID=$(curl -s "http://metadata.google.internal/computeMetadata/v1/project/project-id" -H "Metadata-Flavor: Google")
    GCS_BUCKET_NAME=$(curl -s "http://metadata.google.internal/computeMetadata/v1/instance/attributes/gcs-bucket" -H "Metadata-Flavor: Google")
    REDISHOST=$(curl -s "http://metadata.google.internal/computeMetadata/v1/instance/attributes/redis-host" -H "Metadata-Flavor: Google")
    REDISPORT=$(curl -s "http://metadata.google.internal/computeMetadata/v1/instance/attributes/redis-port" -H "Metadata-Flavor: Google")
    
    # Install dependencies from apt
    apt-get update
    apt-get install -yq \
        git build-essential supervisor python python-dev python-pip libffi-dev \
        libssl-dev
    
    # Install logging monitor. The monitor will automatically pickup logs send to
    # syslog.
    curl -s "https://storage.googleapis.com/signals-agents/logging/google-fluentd-install.sh" | bash
    service google-fluentd restart &
    
    gcloud storage cp gs://"$GCS_BUCKET_NAME"/gce/app.tar /app.tar
    mkdir -p /app
    tar -x -f /app.tar -C /app
    cd /app
    
    # Install the app dependencies
    pip install --upgrade pip virtualenv
    virtualenv /app/env
    /app/env/bin/pip install -r /app/requirements.txt
    
    # Create a pythonapp user. The application will run as this user.
    getent passwd pythonapp || useradd -m -d /home/pythonapp pythonapp
    chown -R pythonapp:pythonapp /app
    
    # Configure supervisor to run the app.
    cat >/etc/supervisor/conf.d/pythonapp.conf << EOF
    [program:pythonapp]
    directory=/app
    environment=HOME="/home/pythonapp",USER="pythonapp",REDISHOST=$REDISHOST,REDISPORT=$REDISPORT
    command=/app/env/bin/gunicorn main:app --bind 0.0.0:8080
    autostart=true
    autorestart=true
    user=pythonapp
    stdout_logfile=syslog
    stderr_logfile=syslog
    EOF
    
    supervisorctl reread
    supervisorctl update

It may take several minutes for the sample application to deploy on the newly created Compute Engine instance.

Once the instance is ready and the startup script has completed execution, go to the [Compute Engine instances page](https://console.cloud.google.com/compute/instances) and copy the **External Ip** address.

To view the sample app you deployed, visit http://[EXTERNAL-IP]:8080

You can use the `teardown.sh` script to delete the instance and firewall created by the deployment script:
    
    
    gcloud compute instances delete my-instance
    
    gcloud compute firewall-rules delete allow-http-server-8080

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
