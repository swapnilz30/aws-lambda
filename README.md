# aws-lambda
TO RUN Lambda function using layer check the following points.
1. Go https://github.com/keithrozario/Klayers repository to the API section.
2. According to region select the API. For example for us-east-1 region select <b>"https://api.klayers.cloud/api/v2/p3.9/layers/latest/us-east-1/"</b> URL.
3. Modify the URL to <b>https://api.klayers.cloud/api/v2/p3.9/layers/latest/us-east-1/json</b> and search pillow.
4. Copy <b>"arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p39-pillow:1"</b> arn and added to lambda function layer.</br>

<h2>Check the following instructions for <b>"python-s3-thumbnail-lambda"</b> function</h2>
1. Create the Access and Secret Keys for the AWS user account. <br>
2. Install sls, serverless-python-requirements (use <b>sls plugin install -n serverless-python-requirements</b>"" command to install this plugin) <br>
3. Clone this repository. <br>
4. run the "sls deploy" command to deploy on AWS.
