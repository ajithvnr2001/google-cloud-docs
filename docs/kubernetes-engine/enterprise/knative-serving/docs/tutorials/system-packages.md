---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tutorials/system-packages/
title: Using system packages \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:21:32.647061+00:00
---

# Using system packages  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tutorials/system-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Using system packages Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to build a custom [Knative serving](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview) service that transforms a graph description input parameter into a diagram in the `PNG` image format. It uses [Graphviz](http://www.graphviz.org/) that is installed as a system package in the service's container environment. Graphviz is used via command-line utilities to serve requests.

## Objectives

  * Write and build a [custom container](https://www.docker.com/resources/what-container) with a [Dockerfile](https://docs.docker.com/engine/reference/builder/)
  * Write, build, and deploy a Knative serving service
  * Use [Graphviz dot](http://www.graphviz.org/documentation/) utility to generate diagrams
  * Test the service by posting a DOT syntax diagram from the collection or your own creation



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Build](https://docs.cloud.google.com/build)
  * [Container Registry](https://docs.cloud.google.com/container-registry)
  * [Knative serving](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

**Caution:** Container Registry is deprecated. Effective March 18, 2025, Container Registry is shut down, and writing images to Container Registry is unavailable. For details on the deprecation and how to migrate to Artifact Registry, see [Container Registry deprecation](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation).

## Before you begin

  * This tutorial assumes that you have Knative serving [installed and configured on your cluster](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install).
  * Ensure that your command-line environment is set up and the tools are up-to-date: 
    * [GKE clusters on Google Cloud](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/command-line-tools)
    * [GKE clusters outside Google Cloud](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp/command-line-tools)



## Retrieving the code sample

To retrieve the code sample for use:

  1. Clone the sample app repository to your local machine:

###  Node.js 
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/archive/master.zip) as a zip file and extract it. 

###  Python 
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/master.zip) as a zip file and extract it. 

###  Go 
         
         git clone https://github.com/GoogleCloudPlatform/golang-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/golang-samples/archive/master.zip) as a zip file and extract it. 

###  Java 
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/java-docs-samples/archive/master.zip) as a zip file and extract it. 

  2. Change to the directory that contains the Knative serving sample code:

###  Node.js 
         
         cd nodejs-docs-samples/run/system-package/

###  Python 
         
         cd python-docs-samples/run/system-package/

###  Go 
         
         cd golang-samples/run/system_package/

###  Java 
         
         cd java-docs-samples/run/system-package/




## Visualizing the architecture

The basic architecture looks like this:

![Diagram showing request flow from user to web service to graphviz dot
    utility.](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/tutorials/images/diagram-as-a-service.png) For the diagram source, see the [ DOT Description](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/tutorials/resources/diagram-as-a-service.dot.txt)

The user makes an HTTP request to the Knative serving service which executes a Graphviz utility to transform the request into an image. That image is delivered to the user as the HTTP response.

## Understanding the code

### Defining your environment configuration with the `Dockerfile`

**Key Point:** Use your `Dockerfile` to customize your environment with libraries, utilities, environment variables, configuration files, and startup processes. This is the container-based approach for "server configuration".

Your `Dockerfile` is specific to the language and base operating environment, such as Ubuntu, that your service will use.

**Note:** the [quickstart](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/deploy-application), although it is for Knative serving, does show various `Dockerfiles` you can use as a starting point to build a `Dockerfile` for other services.

This service requires one or more additional system packages not available by default.

  1. Open the `Dockerfile` in an editor.

  2. Look for a `Dockerfile` [`RUN`](https://docs.docker.com/engine/reference/builder/#run) statement. This statement allows running arbitrary shell commands to modify the environment. If the `Dockerfile` has multiple stages, identified by finding multiple `FROM` statements, it will be found in the last stage.

The specific packages required and the mechanism to install them varies by the operating system declared inside the container.

To get instructions for your operating system or base image, click the appropriate tab.

Debian/Ubuntu
         
         RUN apt-get update -y && apt-get install -y \
           graphviz \
           && apt-get clean

Alpine Alpine requires a second package for font support. 
         
         RUN apk --no-cache add graphviz

To determine the operating system of your container image, check the name in the `FROM` statement or a README associated with your base image. For example, if you extend from `node`, you can find documentation and the parent `Dockerfile` on [Docker Hub](http://hub.docker.com/_/node).

  3. Test your customization by building the image, using [`docker build` locally](https://docs.cloud.google.com/run/docs/building/containers#building_locally_and_pushing_using_docker) or Cloud Build.




### Handling incoming requests

The sample service uses parameters from the incoming HTTP request to invoke a system call that executes the appropriate `dot` utility command.

In the HTTP handler below, a graph description input parameter is extracted from the `dot` querystring variable.

Graph descriptions can include characters which must be [URL encoded](https://wikipedia.org/wiki/Query_string#URL_encoding) for use in a querystring.

###  Node.js 
    
    
    app.get('/diagram.png', (req, res) => {
      try {
        const image = createDiagram(req.query.dot);
        res.setHeader('Content-Type', 'image/png');
        res.setHeader('Content-Length', image.length);
        res.setHeader('Cache-Control', 'public, max-age=86400');
        res.send(image);
      } catch (err) {
        console.error(`error: ${err.message}`);
        const errDetails = (err.stderr || err.message).toString();
        if (errDetails.includes('syntax')) {
          res.status(400).send(`Bad Request: ${err.message}`);
        } else {
          res.status(500).send('Internal Server Error');
        }
      }
    });

###  Python 
    
    
    @app.route("/diagram.png", methods=["GET"])
    def index():
        """Takes an HTTP GET request with query param dot and
        returns a png with the rendered DOT diagram in a HTTP response.
        """
        try:
            image = create_diagram(request.args.get("dot"))
            response = make_response(image)
            response.headers.set("Content-Type", "image/png")
            return response
    
        except Exception as e:
            print(f"error: {e}")
    
            # If no graphviz definition or bad graphviz def, return 400
            if "syntax" in str(e):
                return f"Bad Request: {e}", 400
    
            return "Internal Server Error", 500
    
    

###  Go 
    
    
    // diagramHandler renders a diagram using HTTP request parameters and the dot command.
    func diagramHandler(w http.ResponseWriter, r *http.Request) {
    	if r.Method != http.MethodGet {
    		log.Printf("method not allowed: %s", r.Method)
    		http.Error(w, fmt.Sprintf("HTTP Method %s Not Allowed", r.Method), http.StatusMethodNotAllowed)
    		return
    	}
    
    	q := r.URL.Query()
    	dot := q.Get("dot")
    	if dot == "" {
    		log.Print("no graphviz definition provided")
    		http.Error(w, "Bad Request", http.StatusBadRequest)
    		return
    	}
    
    	// Cache header must be set before writing a response.
    	w.Header().Set("Cache-Control", "public, max-age=86400")
    
    	input := strings.NewReader(dot)
    	if err := createDiagram(w, input); err != nil {
    		log.Printf("createDiagram: %v", err)
    		// Do not cache error responses.
    		w.Header().Del("Cache-Control")
    		if strings.Contains(err.Error(), "syntax") {
    			http.Error(w, "Bad Request: DOT syntax error", http.StatusBadRequest)
    		} else {
    			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
    		}
    	}
    }
    

###  Java 
    
    
    get(
        "/diagram.png",
        (req, res) -> {
          InputStream image = null;
          try {
            String dot = req.queryParams("dot");
            image = createDiagram(dot);
            res.header("Content-Type", "image/png");
            res.header("Content-Length", Integer.toString(image.available()));
            res.header("Cache-Control", "public, max-age=86400");
          } catch (Exception e) {
            if (e.getMessage().contains("syntax")) {
              res.status(400);
              return String.format("Bad Request: %s", e.getMessage());
            } else {
              res.status(500);
              return "Internal Server Error";
            }
          }
          return image;
        });

You'll need to differentiate between internal server errors and invalid user input. This sample service returns an Internal Server Error for all dot command-line errors unless the error message contains the string `syntax`, which indicates a user input problem.

### Generating a diagram

The core logic of diagram generation uses the dot command-line tool to process the graph description input parameter into a diagram in the PNG image format.

###  Node.js 
    
    
    // Generate a diagram based on a graphviz DOT diagram description.
    const createDiagram = dot => {
      if (!dot) {
        throw new Error('syntax: no graphviz definition provided');
      }
    
      // Adds a watermark to the dot graphic.
      const dotFlags = [
        '-Glabel="Made on Cloud Run"',
        '-Gfontsize=10',
        '-Glabeljust=right',
        '-Glabelloc=bottom',
        '-Gfontcolor=gray',
      ].join(' ');
    
      const image = execSync(`/usr/bin/dot ${dotFlags} -Tpng`, {
        input: dot,
      });
      return image;
    };

###  Python 
    
    
    def create_diagram(dot):
        """Generates a diagram based on a graphviz DOT diagram description.
    
        Args:
            dot: diagram description in graphviz DOT syntax
    
        Returns:
            A diagram in the PNG image format.
        """
        if not dot:
            raise Exception("syntax: no graphviz definition provided")
    
        dot_args = [  # These args add a watermark to the dot graphic.
            "-Glabel=Made on Cloud Run",
            "-Gfontsize=10",
            "-Glabeljust=right",
            "-Glabelloc=bottom",
            "-Gfontcolor=gray",
            "-Tpng",
        ]
    
        # Uses local `dot` binary from Graphviz:
        # https://graphviz.gitlab.io
        image = subprocess.run(
            ["dot"] + dot_args, input=dot.encode("utf-8"), stdout=subprocess.PIPE
        ).stdout
    
        if not image:
            raise Exception("syntax: bad graphviz definition provided")
        return image
    
    

###  Go 
    
    
    // createDiagram generates a diagram image from the provided io.Reader written to the io.Writer.
    func createDiagram(w io.Writer, r io.Reader) error {
    	stderr := new(bytes.Buffer)
    	args := []string{
    		"-Glabel=Made on Cloud Run",
    		"-Gfontsize=10",
    		"-Glabeljust=right",
    		"-Glabelloc=bottom",
    		"-Gfontcolor=gray",
    		"-Tpng",
    	}
    	cmd := exec.Command("/usr/bin/dot", args...)
    	cmd.Stdin = r
    	cmd.Stdout = w
    	cmd.Stderr = stderr
    
    	if err := cmd.Run(); err != nil {
    		return fmt.Errorf("exec(%s) failed (%w): %s", cmd.Path, err, stderr.String())
    	}
    
    	return nil
    }
    

###  Java 
    
    
    // Generate a diagram based on a graphviz DOT diagram description.
    public static InputStream createDiagram(String dot) {
      if (dot == null || dot.isEmpty()) {
        throw new NullPointerException("syntax: no graphviz definition provided");
      }
      // Adds a watermark to the dot graphic.
      List<String> args = new ArrayList<>();
      args.add("/usr/bin/dot");
      args.add("-Glabel=\"Made on Cloud Run\"");
      args.add("-Gfontsize=10");
      args.add("-Glabeljust=right");
      args.add("-Glabelloc=bottom");
      args.add("-Gfontcolor=gray");
      args.add("-Tpng");
    
      StringBuilder output = new StringBuilder();
      InputStream stdout = null;
      try {
        ProcessBuilder pb = new ProcessBuilder(args);
        Process process = pb.start();
        OutputStream stdin = process.getOutputStream();
        stdout = process.getInputStream();
        // The Graphviz dot program reads from stdin.
        Writer writer = new OutputStreamWriter(stdin, "UTF-8");
        writer.write(dot);
        writer.close();
        process.waitFor();
      } catch (Exception e) {
        System.out.println(e);
      }
      return stdout;
    }

### Designing a secure service

Any vulnerabilities in the `dot` tool are potential vulnerabilities of the web service. You can mitigate this by using up-to-date versions of the `graphviz` package through re-building the container image on a regular basis.

If you extend the current sample to accept user input as command-line parameters, you should protect against [command-injection attacks](https://wikipedia.org/wiki/Code_injection#Shell_injection). Some of the ways to prevent injection attacks include:

  * Mapping inputs to a dictionary of supported parameters
  * Validating inputs match a range of known-safe values, perhaps using regular expressions
  * Escaping inputs to ensure shell syntax is not evaluated



## Shipping the code

To ship your code, you build with Cloud Build, and upload to Container Registry, and deploy to Knative serving:

  1. Run the following command to build your container and publish on Container Registry.

###  Node.js 
         
         gcloud builds submit --tag gcr.io/PROJECT_ID/graphviz

Where PROJECT_ID is your Google Cloud project ID, and `graphviz` is the name you want to give your service.

Upon success, you will see a SUCCESS message containing the ID, creation time, and image name. The image is stored in Container Registry and can be re-used if desired. 

###  Python 
         
         gcloud builds submit --tag gcr.io/PROJECT_ID/graphviz

Where PROJECT_ID is your Google Cloud project ID, and `graphviz` is the name you want to give your service.

Upon success, you will see a SUCCESS message containing the ID, creation time, and image name. The image is stored in Container Registry and can be re-used if desired. 

###  Go 
         
         gcloud builds submit --tag gcr.io/PROJECT_ID/graphviz

Where PROJECT_ID is your Google Cloud project ID, and `graphviz` is the name you want to give your service.

Upon success, you will see a SUCCESS message containing the ID, creation time, and image name. The image is stored in Container Registry and can be re-used if desired. 

###  Java 

This sample uses [Jib](https://github.com/GoogleContainerTools/jib) to build Docker images using common Java tools. Jib optimizes container builds without the need for a Dockerfile or having [Docker](https://www.docker.com/) installed. 
     1. Using the Dockerfile, configure and build a base image with the system packages installed to override Jib's default base image:
            
            # Use the Official eclipse-temurin image for a lean production stage of our multi-stage build.
            # https://hub.docker.com/_/eclipse-temurin/
            FROM eclipse-temurin:17.0.18_8-jre
            
            RUN apt-get update -y && apt-get install -y \
              graphviz \
              && apt-get clean
            
            gcloud builds submit --tag gcr.io/PROJECT_ID/graphviz-base

Where PROJECT_ID is your Google Cloud project ID.

     2. Build your final container with Jib and publish on Container Registry:
            
            <plugin>
              <groupId>com.google.cloud.tools</groupId>
              <artifactId>jib-maven-plugin</artifactId>
              <version>3.4.0</version>
              <configuration>
                <from>
                  <image>gcr.io/PROJECT_ID/graphviz-base</image>
                </from>
                <to>
                  <image>gcr.io/PROJECT_ID/graphviz</image>
                </to>
              </configuration>
            </plugin>
            
            mvn compile jib:build \
             -Dimage=gcr.io/PROJECT_ID/graphviz \
             -Djib.from.image=gcr.io/PROJECT_ID/graphviz-base

Where PROJECT_ID is your Google Cloud project ID.

  2. Deploy using the following command:
         
         gcloud run deploy graphviz-web --create-if-missing --image gcr.io/PROJECT_ID/graphviz

Where PROJECT_ID is your Google Cloud project ID, and `graphviz` is the name of the container from above and `graphviz-web` is the name of the service.

Wait until the deployment is complete: this can take about half a minute.

  3. If you want to deploy a code update to the service, repeat the previous steps. Each deployment to a service creates a new revision and automatically starts serving traffic when ready.




## Try it out

Try out your service by sending HTTP `POST` requests with DOT syntax descriptions in the request payload.

  1. Send an HTTP request to your service.

You can embed the diagram in a web page:

     1. To obtain the external IP for the Load Balancer, run the following command:
            
            kubectl get svc istio-ingressgateway -n ASM-INGRESS-NAMESPACE

Replace ASM-INGRESS-NAMESPACE with the namespace where your Cloud Service Mesh ingress is located. Specify `istio-system` if you installed Cloud Service Mesh using its default configuration.

The resulting output looks similar to the following:
            
            NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP  PORT(S)
            istio-ingressgateway   LoadBalancer   XX.XX.XXX.XX   pending      80:32380/TCP,443:32390/TCP,32400:32400/TCP

where the **EXTERNAL-IP** value is your external IP address of the Load Balancer.

     2. Run a curl command using this `EXTERNAL-IP` address in the URL. Do not include the protocol (e.g.: `http://`) in `SERVICE_DOMAIN`.
            
            curl -G -H "Host: SERVICE_DOMAIN" http://EXTERNAL-IP/diagram.png \
               --data-urlencode "dot=digraph Run { rankdir=LR Code -> Build -> Deploy -> Run }" \
               > diagram.png

  2. Open the resulting `diagram.png` file in any application that supports `PNG` files, such as Chrome.

It should look like this:

![Diagram showing the stage flow
  of Code to Build to Deploy to 'Run'.](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/knative-serving/docs/tutorials/images/hello-cloud-run.png) Source: [ DOT Description](https://github.com/GoogleCloudPlatform/golang-samples/blob/master/run/system_package/library/hello-cloud-run.dot)



You can explore a small collection of [ready-made diagram descriptions](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/run/system_package/library).

  1. Copy the contents of the selected `.dot` file
  2. Paste it into a `curl` command:
         
         curl -G -H "Host: SERVICE_DOMAIN" http://EXTERNAL-IP/diagram.png \
         --data-urlencode "dot=digraph Run { rankdir=LR Code -> Build -> Deploy -> Run }" \
         > diagram.png




## Clean up

You can delete the resources created for this tutorial to avoid incurring costs.

### Deleting tutorial resources

  1. Delete the Knative serving service you deployed in this tutorial:
         
         gcloud run services delete SERVICE-NAME

Where SERVICE-NAME is your chosen service name.

You can also delete Knative serving services from the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Remove the gcloud default configurations you added during the tutorial setup:
         
         gcloud config unset run/platform
          gcloud config unset run/cluster
          gcloud config unset run/cluster_location
         

  3. Remove the project configuration:
         
         gcloud config unset project
         

  4. Delete other Google Cloud resources created in this tutorial:

     * [Delete the container image](https://docs.cloud.google.com/container-registry/docs/managing#deleting_images) named `gcr.io/<var>PROJECT_ID</var>/graphviz` from Container Registry.
     * If you created a cluster for this tutorial, [delete the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster). 



## What's next

  * Experiment with your graphviz app: 
    * Add support for other graphviz utilities which apply different algorithms to diagram generation.
    * Save diagrams to [Cloud Storage](https://docs.cloud.google.com/storage). Do you want to save the image or the DOT syntax?
    * Implement content abuse protection with [Cloud Natural Language API](https://docs.cloud.google.com/natural-language).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
