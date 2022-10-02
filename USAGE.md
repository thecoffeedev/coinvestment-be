# API usage

## :heavy_exclamation_mark: Request failure
> ## Note
> When a request has failed the response will be formatted as below, 
> with the `statusCode` key being `FAILURE` and the `statusMessage` 
> showing the reason for the failure. `FAILURE` does not mean the 
> request was not received, but the request received could not be
> completed. These failure messages can be shown in the front-end or
> be interpreted by the developer as to how to handle the failure and
> an alternative user-friendly message can be displayed.
>  
>> Examples of failure could be:
>> * Incorrectly formatted request JSON
>> * Unauthenticated credentials
>> * Attempted access to unauthorized routes
>> * Incorrectly formatted data (email address, password length, etc.)

### Request failure response
```json
{
    "status": {
        "statusCode": "FAILURE",
        "statusMessage" : "<The reason for the failure>"
    }
}
```



