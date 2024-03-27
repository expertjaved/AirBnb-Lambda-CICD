# AirBnb-Lambda-CICD
this repo is for Airbnb project


The buildspec.yml you provided is designed to create and configure the entire Airbnb booking data pipeline infrastructure from scratch using the AWS CLI commands. It doesn't require you to provide any URLs or ARNs as input because it will create the required resources and capture their URLs/ARNs during the build process.

Here's a breakdown of what the buildspec.yml does:

    Install Phase: Installs the AWS CLI and the Boto3 Python library, which will be used to interact with AWS services.
    Build Phase:
        Creates the AirbnbBookingQueue and AirbnbBookingDLQ SQS queues.
        Configures the AirbnbBookingQueue to send messages to the AirbnbBookingDLQ after 3 unsuccessful delivery attempts.
        Creates the ProduceAirbnbBookingData Lambda function from a local producer_lambda.zip file.
        Creates the ProcessFilteredBookings Lambda function from a local destination_lambda.zip file.
        Creates an EventBridge rule named FilteredBookingRule to trigger the ProcessFilteredBookings Lambda function when a message is sent to the AirbnbBookingQueue.
        Creates an EventBridge pipe named AirbnbBookingPipe to consume messages from the AirbnbBookingQueue.
        Configures the AirbnbBookingPipe to filter messages where the booking duration is greater than 1 day and send them to the ProcessFilteredBookings Lambda function.
    Post-Build Phase: Cleans up the temporary producer_lambda.zip and destination_lambda.zip files.

Note that you'll need to replace the following placeholders in the buildspec.yml file with your actual values:

    <producer_lambda_role_arn>: The ARN of the IAM role that the ProduceAirbnbBookingData Lambda function will assume.
   
   Replace <enrichment_lambda_role_arn> with the ARN of the IAM role that the EnrichAirbnbBookingData Lambda function will assume

    <destination_lambda_role_arn>: The ARN of the IAM role that the ProcessFilteredBookings Lambda function will assume.

Additionally, you'll need to include the producer_lambda.zip and destination_lambda.zip files containing your Lambda function code in the same directory as the buildspec.yml file.

When you run this CodeBuild project, it will create the entire infrastructure described in the assignment, including the SQS queues, Lambda functions, EventBridge rule, and EventBridge pipe. You don't need to provide any URLs or ARNs upfront, as the build process will create and capture them automatically.