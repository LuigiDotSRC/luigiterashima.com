<p>welcome to my corner of the internet! occasionally i will post about about latest achievements, computer programming+projects, great reads, and other random stuff.</p>
<h3>my website:</h3>
<p>frontend is built using html, css, and javascript. all static files are hosted on an Amazon S3 instance which is connected to an Amazon Cloudfront distribution so that edge locations can access my website with low latency. i created and configured my own domain using Amazon Route 53 alongside Amazon Certificate Manager which provides an SSL certificate enabling https connections.</p>
<p>to store and retrieve blog posts i configured a free supabase database and implemented the postgREST APIs into my website to display my blogs dynamically.</p>
<p>to deploy changes to my website and create new blogs i created some python scripts using the boto3 and supabase python SDK.
<p>my website source code is available on <a href="https://github.com/LuigiDotSRC/luigiterashima.com/">github</a><p>

<img src="https://s3.amazonaws.com/luigiterashima.com-images/website-architecture.png">