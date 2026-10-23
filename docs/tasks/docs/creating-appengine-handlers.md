---
url: https://docs.cloud.google.com/tasks/docs/creating-appengine-handlers/
title: Create App Engine task handlers \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:33.487458+00:00
---

# Create App Engine task handlers  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/creating-appengine-handlers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Create App Engine task handlers Stay organized with collections  Save and categorize content based on your preferences. 

This page demonstrates how to create an App Engine _task handler_ , the worker code that handles an App Engine task. The Cloud Tasks queue sends HTTP requests to your task handler. Upon successful completion of processing, the handler must send an HTTP status code between `200` and `299` back to the queue. Any other value indicates the task has failed and the queue retries the task.

**Note:** App Engine itself returns a `503` status code when instances are overloaded or otherwise unavailable. The Task service responds to this by slowing delivery from queues to handlers, to avoid making the problem worse. If you want to trigger a retry intentionally, use any status code _other_ than `2xx` or `503`.

App Engine Task Queue requests are sent from the IP address `0.1.0.2`. Also refer to the [IP range for requests sent to the App Engine environment](https://docs.cloud.google.com/tasks/docs/creating-appengine-tasks#firewall_rules).

###  C# 
    
    
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }
    
        public IConfiguration Configuration { get; }
    
        // This method gets called by the runtime. Use this method to add services to the container.
        // For more information on how to configure your application, visit https://go.microsoft.com/fwlink/?LinkID=398940
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddLogging(builder => builder.AddDebug());
            services.AddRouting();
        }
    
        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IHostingEnvironment env, ILoggerFactory loggerFactory)
        {
            var logger = loggerFactory.CreateLogger("testStackdriverLogging");
    
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
            else
            {
                // Configure error reporting service.
                app.UseExceptionHandler("/Home/Error");
            }
    
            var routeBuilder = new RouteBuilder(app);
    
            routeBuilder.MapPost("log_payload", context =>
            {
                // Log the request payload
                var reader = new StreamReader(context.Request.Body);
                var task = reader.ReadToEnd();
    
                logger.LogInformation($"Received task with payload: {task}");
                return context.Response.WriteAsync($"Printed task payload: {task}");
            });
    
            routeBuilder.MapGet("hello", context =>
            {
                // Basic index to verify app is serving
                return context.Response.WriteAsync("Hello, world!");
            });
    
            routeBuilder.MapGet("_ah/health", context =>
            {
                // Respond to GAE health-checks
                return context.Response.WriteAsync("OK");
            });
    
            routeBuilder.MapGet("/", context =>
            {
                return context.Response.WriteAsync("Hello, world!");
            });
    
            var routes = routeBuilder.Build();
            app.UseRouter(routes);
        }
    }
    

###  Go 
    
    
    // Sample task_handler is an App Engine app demonstrating Cloud Tasks handling.
    package main
    
    import (
    	"fmt"
    	"io"
    	"log"
    	"net/http"
    	"os"
    )
    
    func main() {
    	// Allow confirmation the task handling service is running.
    	http.HandleFunc("/", indexHandler)
    
    	// Handle all tasks.
    	http.HandleFunc("/task_handler", taskHandler)
    
    	port := os.Getenv("PORT")
    	if port == "" {
    		port = "8080"
    		log.Printf("Defaulting to port %s", port)
    	}
    
    	log.Printf("Listening on port %s", port)
    	if err := http.ListenAndServe(":"+port, nil); err != nil {
    		log.Fatal(err)
    	}
    }
    
    // indexHandler responds to requests with our greeting.
    func indexHandler(w http.ResponseWriter, r *http.Request) {
    	if r.URL.Path != "/" {
    		http.NotFound(w, r)
    		return
    	}
    	fmt.Fprint(w, "Hello, World!")
    }
    
    // taskHandler processes task requests.
    func taskHandler(w http.ResponseWriter, r *http.Request) {
    	taskName := r.Header.Get("X-Appengine-Taskname")
    	if taskName == "" {
    		// You may use the presence of the X-Appengine-Taskname header to validate
    		// the request comes from Cloud Tasks.
    		log.Println("Invalid Task: No X-Appengine-Taskname request header found")
    		http.Error(w, "Bad Request - Invalid Task", http.StatusBadRequest)
    		return
    	}
    
    	// Pull useful headers from Task request.
    	queueName := r.Header.Get("X-Appengine-Queuename")
    
    	// Extract the request body for further task details.
    	body, err := io.ReadAll(r.Body)
    	if err != nil {
    		log.Printf("ReadAll: %v", err)
    		http.Error(w, "Internal Error", http.StatusInternalServerError)
    		return
    	}
    
    	// Log & output details of the task.
    	output := fmt.Sprintf("Completed task: task queue(%s), task name(%s), payload(%s)",
    		queueName,
    		taskName,
    		string(body),
    	)
    	log.Println(output)
    
    	// Set a non-2xx status code to indicate a failure in task processing that should be retried.
    	// For example, http.Error(w, "Internal Server Error: Task Processing", http.StatusInternalServerError)
    	fmt.Fprintln(w, output)
    }
    

###  Java 
    
    
    @WebServlet(
        name = "Tasks",
        description = "Create Cloud Task",
        urlPatterns = "/tasks/create"
    )
    public class TaskServlet extends HttpServlet {
      private static Logger log = Logger.getLogger(TaskServlet.class.getName());
    
      @Override
      public void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        log.info("Received task request: " + req.getServletPath());
        String body = req.getReader()
            .lines()
            .reduce("", (accumulator, actual) -> accumulator + actual);
    
        if (!body.isEmpty()) {
          log.info("Request payload: " + body);
          String output = String.format("Received task with payload %s", body);
          resp.getOutputStream().write(output.getBytes());
          log.info("Sending response: " + output);
          resp.setStatus(HttpServletResponse.SC_OK);
        } else {
          log.warning("Null payload received in request to " + req.getServletPath());
        }
      }
    }

###  Node.js 
    
    
    const express = require('express');
    
    const app = express();
    app.enable('trust proxy');
    
    // Set the Content-Type of the Cloud Task to ensure compatibility
    // By default, the Content-Type header of the Task request is set to "application/octet-stream"
    // see https://cloud.google.com/tasks/docs/reference/rest/v2beta3/projects.locations.queues.tasks#AppEngineHttpRequest
    app.use(express.text());
    
    app.get('/', (req, res) => {
      // Basic index to verify app is serving
      res.send('Hello, World!').end();
    });
    
    app.post('/log_payload', (req, res) => {
      // Log the request payload
      console.log(`Received task with payload: ${req.body}`);
      res.send(`Printed task payload: ${req.body}`).end();
    });
    
    app.get('*', (req, res) => {
      res.send('OK').end();
    });
    
    const PORT = process.env.PORT || 8080;
    app.listen(PORT, () => {
      console.log(`App listening on port ${PORT}`);
      console.log('Press Ctrl+C to quit.');
    });

###  PHP 
    
    
    require __DIR__ . '/vendor/autoload.php';
    
    use Google\Cloud\Logging\LoggingClient;
    
    // Create the logging client.
    $logging = new LoggingClient();
    // Create a PSR-3-compatible logger.
    $logger = $logging->psrLogger('app', ['batchEnabled' => true]);
    
    // Front-controller to route requests.
    switch (@parse_url($_SERVER['REQUEST_URI'])['path']) {
        case '/':
            print "Hello, World!\n";
            break;
        case '/task_handler':
            // Taskname and Queuename are two of several useful Cloud Tasks headers available on the request.
            $taskName = $_SERVER['HTTP_X_APPENGINE_TASKNAME'] ?? '';
            $queueName = $_SERVER['HTTP_X_APPENGINE_QUEUENAME'] ?? '';
    
            try {
                handle_task(
                    $queueName,
                    $taskName,
                    file_get_contents('php://input')
                );
            } catch (Exception $e) {
                http_response_code(400);
                exit($e->getMessage());
            }
            break;
        default:
            http_response_code(404);
            exit('Not Found');
    }
    
    /**
     * Process a Cloud Tasks HTTP Request.
     *
     * @param string $queueName provides the name of the queue which dispatched the task.
     * @param string $taskName provides the identifier of the task.
     * @param string $body The task details from the HTTP request.
     */
    function handle_task($queueName, $taskName, $body = '')
    {
        global $logger;
    
        if (empty($taskName)) {
            // You may use the presence of the X-Appengine-Taskname header to validate
            // the request comes from Cloud Tasks.
            $logger->warning('Invalid Task: No X-Appengine-Taskname request header found');
            throw new Exception('Bad Request - Invalid Task');
        }
    
        $output = sprintf('Completed task: task queue(%s), task name(%s), payload(%s)', $queueName, $taskName, $body);
        $logger->info($output);
    
        // Set a non-2xx status code to indicate a failure in task processing that should be retried.
        // For example, http_response_code(500) to indicate a server error.
        print $output;
    }
    

###  Python 
    
    
    from flask import Flask, render_template, request
    
    app = Flask(__name__)
    
    
    @app.route("/example_task_handler", methods=["POST"])
    def example_task_handler():
        """Log the request payload."""
        payload = request.get_data(as_text=True) or "(empty payload)"
        print(f"Received task with payload: {payload}")
        return render_template("index.html", payload=payload)
    
    

###  Ruby 
    
    
    require "sinatra"
    require "json"
    
    get "/" do
      # Basic index to verify app is serving
      "Hello World!"
    end
    
    post "/log_payload" do
      data = request.body.read
      # Log the request payload
      puts "Received task with payload: #{data}"
      "Printed task payload: #{data}"
    end

## Timeouts

App Engine tasks have specific timeouts that depend on the [scaling type](https://docs.cloud.google.com/appengine/docs/standard/python/how-instances-are-managed#instance_scaling) of the service that's running them.

For worker services running in the standard environment:

  * Automatic scaling: task processing must finish in 10 minutes.
  * Manual and basic scaling: requests can run up to 24 hours.



For worker services running in the flex environment: all types have a 60 minute timeout.

If your handler misses the deadline, the queue assumes the task failed and retries it.

**Note:** You should consider whether your handler is [idempotent](https://wikipedia.org/wiki/idempotent). Cloud Tasks is designed to provide "at least once" delivery; that is, if a task is successfully added, the queue will deliver it at least once. Note that in some rare circumstances, multiple task execution is possible, so your code must ensure that there are no harmful side-effects of repeated execution.

## Reading App Engine task request headers

Requests sent to your App Engine handler by a Cloud Tasks queue have special headers, which contain task-specific information your handler might want to use.

These headers are set internally. If any of these headers are present in an external user request to your app, they are replaced by the internal ones — except for requests from logged in administrators of the application, who are allowed to set headers for testing purposes.

App Engine task requests always contain the following headers:

Header | Description  
---|---  
`X-AppEngine-QueueName` | The name of the queue.  
`X-AppEngine-TaskName` | The "short" name of the task, or, if no name was specified at creation, a unique system-generated id. This is the `my-task-id` value in the complete task name; for example, `task_name` = `projects/my-project-id/locations/my-location/queues/my-queue-id/tasks/my-task-id`.  
`X-AppEngine-TaskRetryCount` | The number of times that the task has been retried. For the first attempt, this value is `0`. This number includes attempts where the task failed due to a lack of available instances and never reached the execution phase.  
`X-AppEngine-TaskExecutionCount` | The number of times that the task has executed and received a response from the handler. Since Cloud Tasks deletes the task once a successful response has been received, all previous handler responses are failures. This number does not include failures due to a lack of available instances. Note that `X-AppEngine-TaskExecutionCount` can be equal to `X-AppEngine-TaskRetryCount` if it is updated before an execution is attempted.  
`X-AppEngine-TaskETA` | Initially, the originally scheduled time of the task, specified in seconds since January 1st 1970. Note that it represents the expected dispatch time. On retries, it is updated closer to the current time and can be used to measure delivery latency. It should _not_ be used for [task deduplication](https://docs.cloud.google.com/tasks/docs/dual-overview#task_deduplication).  
  
If your request handler finds any of the headers listed previously, it can assume that the request is a Cloud Tasks request.

In addition, requests from Cloud Tasks might contain the following headers:

Header | Description  
---|---  
`X-AppEngine-TaskPreviousResponse` | The HTTP response code from the previous retry.  
`X-AppEngine-TaskRetryReason` | The reason for retrying the task.  
`X-AppEngine-FailFast` | Indicates that a task fails immediately if an existing instance is not available.  
  
## Target routing

In App Engine tasks, both the queue and the task handler run within the same Google Cloud project. Traffic is encrypted during transport and never leaves Google datacenters. You cannot explicitly set the protocol (for example, HTTP or HTTPS). The request to the handler, however, will _appear_ to have used the HTTP protocol.

Tasks can be dispatched to secure task handlers, unsecure task handlers, and in supported runtimes, URIs restricted with [`login: admin`](https://docs.cloud.google.com/appengine/docs/standard/python/config/appref#handlers_login). Because tasks are not run as any user, they _cannot_ be dispatched to URIs restricted with [`login: required`](https://docs.cloud.google.com/appengine/docs/standard/python/config/appref#handlers_login). Task dispatches also don't follow redirects.

## What's next

  * Learn more about tasks in the [RPC API reference](https://docs.cloud.google.com/tasks/docs/reference/rpc).
  * Learn more about tasks in the [REST API reference](https://docs.cloud.google.com/tasks/docs/reference/rest). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
