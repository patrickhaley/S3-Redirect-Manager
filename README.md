# S3-Redirect-Manager

S3-Redirect-Manager is a tool that helps manage URL redirects for an S3-hosted static website. It allows you to define redirects in a CSV file and convert them into the JSON format required by AWS S3 for static website hosting redirection rules.

## Features

- Easily manage URL redirects in a spreadsheet.
- Convert CSV data to the JSON format needed for S3 redirection rules.
- Supports bulk redirects for large-scale URL management.

## Prerequisites

- Python 3.x
- Pandas library (optional, for handling larger datasets)

## Installation

1. **Clone the Repository**:
    ```
    git clone https://github.com/yourusername/S3-Redirect-Manager.git
    cd S3-Redirect-Manager
    ```
2. **Install Required Libraries**:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare the CSV File**:
    - Create a CSV file named `redirects.csv` with the following columns:
        - **Old Path**: The old URL path to redirect from.
        - **New Path**: The new URL path to redirect to.
        - **Protocol**: The protocol to use for the redirect (e.g., https).
        - **Status Code**: The HTTP status code for the redirect (e.g., 301).

    Example **redirects.csv**:

    ```
    Old Path,New Path,Protocol,Status Code
    old-path-1,new-path-1,https,301
    old-path-2,new-path-2,https,301
    ```

2. **Convert CSV to JSON**:
    - Update the Python script to set the new domain.
    - Run the Python script to convert the CSV file to a JSON configuration:
    ```
    python csv_to_json.py
    ```
    - This will generate a file named `website-configuration.json`.

3. **Upload the JSON Configuration to S3**:
    - Go to your S3 bucket in the AWS Management Console.
    - Navigate to the "Properties" tab.
    - Edit the "Static website hosting" section.
    - Paste the contents of `website-configuration.json` into the "Redirection rules" editor and save.

## Setting Up S3 Static Website Hosting

1. **Create an S3 Bucket**:
    - Go to the S3 console in AWS.
    - Create a new bucket named `old.domain.com` (replace with your old domain being redirected to the new domain). 

2. **Enable Static Website Hosting**:
    - Select your bucket.
    - Go to the "Properties" tab.
    - Click "Edit" in the "Static website hosting" section.
    - Choose "Enable" under "Static website hosting".
    - Leave the "Index document" and "Error document" fields empty.

3. **Configure Redirection Rules**:
    - Use the generated `website-configuration.json` file to configure redirection rules.
    - Go to the "Properties" tab of your bucket.
    - Click "Edit" in the "Static website hosting" section.
    - Enable "Use this bucket to host a website".
    - Click "Edit Redirection rules".
    - Paste the JSON configuration from `website-configuration.json` and save.

4. **Set Up Bucket Policy for Public Access**:
    - Go to the "Permissions" tab of your bucket.
    - Click on "Bucket Policy" and add the following policy to allow public read access:

    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "PublicReadGetObject",
          "Effect": "Allow",
          "Principal": "*",
          "Action": "s3:GetObject",
          "Resource": "arn:aws:s3:::old.domain.com/*" // Replace with your old domain being redirected to the new domain
        }
      ]
    }
    ```

5. **Update DNS Settings**:
    - Go to your DNS provider (Route 53 if you are using AWS).
    - Create a new CNAME record for `old.domain.com` pointing to `old.domain.com.s3-website-your-region.amazonaws.com` (replace with your old domain being redirected to the new domain).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
