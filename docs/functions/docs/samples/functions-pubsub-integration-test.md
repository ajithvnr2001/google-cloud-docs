---
url: https://docs.cloud.google.com/functions/docs/samples/functions-pubsub-integration-test/
title: Pub/Sub integration tests \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:52.104275+00:00
---

# Pub/Sub integration tests  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-pubsub-integration-test/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Pub/Sub integration tests Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to integration test a function triggered by Pub/Sub.

## Code sample

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import static com.google.common.truth.Truth.assertThat;
    
    import com.google.gson.Gson;
    import io.github.resilience4j.core.IntervalFunction;
    import io.github.resilience4j.retry.Retry;
    import io.github.resilience4j.retry.RetryConfig;
    import io.github.resilience4j.retry.RetryRegistry;
    import io.vavr.CheckedRunnable;
    import java.io.ByteArrayOutputStream;
    import java.io.File;
    import java.io.IOException;
    import java.io.InputStream;
    import java.net.URI;
    import java.nio.charset.StandardCharsets;
    import java.util.Base64;
    import java.util.Map;
    import java.util.UUID;
    import org.apache.http.client.HttpClient;
    import org.apache.http.client.methods.HttpPost;
    import org.apache.http.conn.HttpHostConnectException;
    import org.apache.http.entity.StringEntity;
    import org.apache.http.impl.client.HttpClientBuilder;
    import org.junit.AfterClass;
    import org.junit.BeforeClass;
    import org.junit.Test;
    
    public class ExampleIT {
      // Each function must be assigned a unique port to run on.
      // Otherwise, tests can flake when 2+ functions run simultaneously.
      // This is also specified in the `function-maven-plugin` config in `pom.xml`.
      private static final int PORT = 8083;
    
      // Root URL pointing to the locally hosted function
      // The Functions Framework Maven plugin lets us run a function locally
      private static final String BASE_URL = "http://localhost:" + PORT;
    
      private static Process emulatorProcess = null;
      private static HttpClient client = HttpClientBuilder.create().build();
      private static final Gson gson = new Gson();
    
      @BeforeClass
      public static void setUp() throws IOException {
        // Get the sample's base directory (the one containing a pom.xml file)
        String baseDir = System.getProperty("user.dir");
    
        // Emulate the function locally by running the Functions Framework Maven plugin
        emulatorProcess = new ProcessBuilder()
            .command("bash", "-c", "mvn function:run")
            .directory(new File(baseDir))
            .start();
      }
    
      @AfterClass
      public static void tearDown() throws IOException {
        // Display the output of the plugin process
        InputStream stdoutStream = emulatorProcess.getInputStream();
        ByteArrayOutputStream stdoutBytes = new ByteArrayOutputStream();
        stdoutBytes.write(stdoutStream.readNBytes(stdoutStream.available()));
        System.err.println(stdoutBytes.toString(StandardCharsets.UTF_8));
    
        // Terminate the running Functions Framework Maven plugin process (if it's still running)
        if (emulatorProcess.isAlive()) {
          emulatorProcess.destroy();
        }
      }
    
      @Test
      public void helloPubSub_shouldRunWithFunctionsFramework() throws Throwable {
        String functionUrl = BASE_URL + "/helloPubsub"; // URL to your locally-running function
    
        // Initialize constants
        String name = UUID.randomUUID().toString();
        String nameBase64 = Base64.getEncoder().encodeToString(name.getBytes(StandardCharsets.UTF_8));
    
        String jsonStr = gson.toJson(Map.of("data", Map.of("data", nameBase64)));
    
        HttpPost postRequest =  new HttpPost(URI.create(functionUrl));
        postRequest.setEntity(new StringEntity(jsonStr));
    
        // The Functions Framework Maven plugin process takes time to start up
        // Use resilience4j to retry the test HTTP request until the plugin responds
        RetryRegistry registry = RetryRegistry.of(RetryConfig.custom()
            .maxAttempts(12)
            .retryExceptions(HttpHostConnectException.class)
            .retryOnResult(u -> {
              // Retry if the Functions Framework process has no stdout content
              // See `retryOnResultPredicate` here: https://resilience4j.readme.io/docs/retry
              try {
                return emulatorProcess.getErrorStream().available() == 0;
              } catch (IOException e) {
                return true;
              }
            })
            .intervalFunction(IntervalFunction.ofExponentialBackoff(200, 2))
            .build());
        Retry retry = registry.retry("my");
    
        // Perform the request-retry process
        CheckedRunnable retriableFunc = Retry.decorateCheckedRunnable(
            retry, () -> client.execute(postRequest));
        retriableFunc.run();
    
        // Get Functions Framework plugin process' stdout
        InputStream stdoutStream = emulatorProcess.getErrorStream();
        ByteArrayOutputStream stdoutBytes = new ByteArrayOutputStream();
        stdoutBytes.write(stdoutStream.readNBytes(stdoutStream.available()));
    
        // Verify desired name value is present
        assertThat(stdoutBytes.toString(StandardCharsets.UTF_8)).contains(
            String.format("Hello %s!", name));
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const assert = require('assert');
    const {spawn} = require('child_process');
    const {request} = require('[gaxios](https://docs.cloud.google.com/nodejs/docs/reference/gaxios/latest/overview.html)');
    const uuid = require('uuid');
    const waitPort = require('wait-port');
    
      it('helloPubSub: should print a name', async () => {
        const name = uuid.v4();
        const PORT = 8088; // Each running framework instance needs a unique port
    
        const encodedName = Buffer.from(name).toString('base64');
        const pubsubMessage = {data: {data: encodedName}};
        const ffProc = spawn('npx', [
          'functions-framework',
          '--target',
          'helloPubSub',
          '--signature-type',
          'event',
          '--port',
          PORT,
        ]);
    
        try {
          const ffProcHandler = new Promise((resolve, reject) => {
            let stdout = '';
            let stderr = '';
            ffProc.stdout.on('data', data => (stdout += data));
            ffProc.stderr.on('data', data => (stderr += data));
            ffProc.on('exit', code => {
              if (code === 0 || code === null) {
                // code === null corresponds to a signal-kill
                // (which doesn't necessarily indicate a test failure)
                resolve(stdout);
              } else {
                stderr = `Error code: ${code}\n${stderr}`;
                reject(new Error(stderr));
              }
            });
          });
          await waitPort({host: 'localhost', port: PORT});
    
          // Send HTTP request simulating Pub/Sub message
          // (GCF translates Pub/Sub messages to HTTP requests internally)
          const response = await request({
            url: `http://localhost:${PORT}/`,
            method: 'POST',
            data: pubsubMessage,
          });
          ffProc.kill();
    
          assert.strictEqual(response.status, 204);
    
          // Wait for the functions framework to stop
          const stdout = await ffProcHandler;
          assert.match(stdout, new RegExp(`Hello, ${name}!`));
        } catch {
          if (ffProc) {
            // Make sure the functions framework is stopped
            ffProc.kill();
          }
        }
      });
    });

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace Google\Cloud\Samples\Functions\HelloworldPubsub;
    
    use Google\CloudFunctions\CloudEvent;
    use GuzzleHttp\Client;
    use PHPUnit\Framework\TestCase;
    use Symfony\Component\Process\Process;
    use Symfony\Component\Process\PhpExecutableFinder;
    
    /**
     * Class SampleIntegrationTest.
     *
     * Integration tests for the 'Helloworld Pubsub' Cloud Function.
     */
    class SampleIntegrationTest extends TestCase
    {
        /** @var Process */
        private static $process;
    
        /** @var Client */
        private static $client;
    
        public function dataProvider()
        {
            return [
                [
                    'cloudevent' => CloudEvent::fromArray([
                        'id' => uniqid(),
                        'source' => 'pubsub.googleapis.com',
                        'specversion' => '1.0',
                        'type' => 'google.cloud.pubsub.topic.v1.messagePublished',
                    ]),
                    'data' => [
                        'data' => base64_encode('John')
                    ],
                    'expected' => 'Hello, John!'
                ],
            ];
        }
    
        /**
         * Start a local PHP server running the Functions Framework.
         *
         * @beforeClass
         */
        public static function startFunctionFramework(): void
        {
            $port = getenv('PORT') ?: '8080';
            $php = (new PhpExecutableFinder())->find();
            $uri = 'localhost:' . $port;
    
            // https://symfony.com/doc/current/components/process.html#usage
            self::$process = new Process([$php, '-S', $uri, 'vendor/bin/router.php'], null, [
                'FUNCTION_SIGNATURE_TYPE' => 'cloudevent',
                'FUNCTION_TARGET' => 'helloworldPubsub',
            ]);
            self::$process->start();
    
            // Initialize an HTTP client to drive requests.
            self::$client = new Client(['base_uri' => 'http://' . $uri]);
    
            // Short delay to ensure PHP server is ready.
            sleep(1);
        }
    
        /**
         * Stop the local PHP server.
         *
         * @afterClass
         */
        public static function stopFunctionFramework(): void
        {
            if (!self::$process->isRunning()) {
                echo self::$process->getErrorOutput();
                throw new RuntimeException('Function Framework PHP process not running by end of test');
            }
            self::$process->stop(3, SIGTERM);
        }
    
        /**
         * @dataProvider dataProvider
         */
        public function testHelloPubsub(
            CloudEvent $cloudevent,
            array $data,
            string $expected
        ): void {
            // Send an HTTP request using CloudEvent metadata.
            $resp = self::$client->post('/', [
                'body' => json_encode($data),
                'headers' => [
                    // Instruct the function framework to parse the body as JSON.
                    'content-type' => 'application/json',
    
                    // Prepare the HTTP headers for a CloudEvent.
                    'ce-id' => $cloudevent->getId(),
                    'ce-source' => $cloudevent->getSource(),
                    'ce-specversion' => $cloudevent->getSpecVersion(),
                    'ce-type' => $cloudevent->getType()
                ],
            ]);
    
            // The Cloud Function logs all data to stderr.
            $actual = self::$process->getIncrementalErrorOutput();
    
            // Verify the function's results are correctly logged.
            $this->assertStringContainsString($expected, $actual);
        }
    }
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    import os
    import subprocess
    import uuid
    
    import requests
    from requests.packages.urllib3.util.retry import Retry
    
    
    def test_print_name():
        name = str(uuid.uuid4())
        port = 8088  # Each running framework instance needs a unique port
    
        encoded_name = base64.b64encode(name.encode("utf-8")).decode("utf-8")
        pubsub_message = {"data": {"data": encoded_name}}
    
        process = subprocess.Popen(
            [
                "functions-framework",
                "--target",
                "hello_pubsub",
                "--signature-type",
                "event",
                "--port",
                str(port),
            ],
            cwd=os.path.dirname(__file__),
            stdout=subprocess.PIPE,
        )
    
        # Send HTTP request simulating Pub/Sub message
        # (GCF translates Pub/Sub messages to HTTP requests internally)
        url = f"http://localhost:{port}/"
    
        retry_policy = Retry(total=6, backoff_factor=1)
        retry_adapter = requests.adapters.HTTPAdapter(max_retries=retry_policy)
    
        session = requests.Session()
        session.mount(url, retry_adapter)
    
        response = session.post(url, json=pubsub_message)
    
        assert response.status_code == 200
    
        # Stop the functions framework process
        process.kill()
        process.wait()
        out, err = process.communicate()
    
        print(out, err, response.content)
    
        assert f"Hello {name}!" in str(out)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
