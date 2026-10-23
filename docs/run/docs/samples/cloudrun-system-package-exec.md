---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-system-package-exec/
title: Generate a diagram with the dot tool from the graphviz package \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:29.837015+00:00
---

# Generate a diagram with the dot tool from the graphviz package  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-system-package-exec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Generate a diagram with the dot tool from the graphviz package Stay organized with collections  Save and categorize content based on your preferences. 

Use a customized Dockerfile to configure system packages whose command-line utilities are used as part of serving HTTP requests.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Using system packages](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tutorials/system-packages)
  * [Using system packages tutorial](https://docs.cloud.google.com/run/docs/tutorials/system-packages)



## Code sample

### Go

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Node.js

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
