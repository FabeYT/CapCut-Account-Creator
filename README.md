# CapCut Signup Automation - README

This script automates the process of signing up for a CapCut account and sends the credentials (email and password) to a Discord webhook. It uses Selenium WebDriver, ChromeDriver, and other dependencies to interact with the CapCut signup page and a temporary email provider to retrieve the verification code.

## Requirements

To run this script, you will need the following:

1. **Python 3.6+**: Make sure Python is installed on your machine.
2. **Chrome browser**: This script is designed to work with Google Chrome. Ensure that you have it installed.
3. **ChromeDriver**: This script uses the ChromeDriver for Selenium. The `webdriver_manager` library automatically installs the correct version.
4. **Libraries**: You need to install the following Python libraries:
    - `selenium`
    - `requests`
    - `webdriver-manager`

You can install the required libraries using pip:

```bash
pip install selenium requests webdriver-manager
```

## Setup

1. **Webhook URL**:
   - Replace the placeholder `WEBHOOK_URL` in the script with your actual Discord webhook URL.
   - You can create a webhook URL by going to your Discord server's settings -> Integrations -> Webhooks.

2. **Verification Email**:
   - This script uses `temp-mail.io` to generate a temporary email address for the signup process.
   - The script automatically switches to the temp-mail tab and retrieves the verification code once the email arrives.

3. **Password**:
   - The script uses the password `BumBum11!`. If you want to change it, modify the following line in the script:
     ```python
     password = "BumBum11!"
     ```

## How to Use

1. **Run the Script**:
   - Open a terminal and navigate to the directory where the script is located.
   - Run the script with Python:
     ```bash
     python capcut_signup.py
     ```

2. **Input the Repeat Count**:
   - When the script is executed, it will prompt you to enter the number of times you want to repeat the signup process.
   - Type the number of iterations and press Enter.

3. **Process Flow**:
   - The script will open the CapCut signup page.
   - It will automatically open a new tab and retrieve a temporary email from `temp-mail.io`.
   - The email will be used as the username for signing up.
   - The script will then fill in the password and proceed with the signup steps.
   - After entering the necessary details, the script will wait for an email with the verification code and enter it automatically once found.
   - Once the signup is complete, it sends the email and password to the specified Discord webhook.

4. **Monitor the Process**:
   - The script will print progress messages in the terminal, so you can monitor what's happening.
   - Once the process is completed, it will print a success message and close the browser.

5. **Error Handling**:
   - If any errors occur, they will be displayed in the terminal.
   - The script will retry certain steps (e.g., waiting for the "Next" button to become enabled or waiting for the verification email).

## Example Output

```bash
░█████╗░░█████╗░░█████╗░██████╗░░█████╗░██╗░░░██╗████████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝
██║░░╚═╝███████║██║░░╚═╝██████╔╝██║░░╚═╝██║░░░██║░░░██║░░░
██║░░██╗██╔══██║██║░░██╗██╔═══╝░██║░░██╗██║░░░██║░░░██║░░░
╚█████╔╝██║░░██║╚█████╔╝██║░░░░░╚█████╔╝╚██████╔╝░░░██║░░░
░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░░╚════╝░░╚═════╝░░░░╚═╝░░░
Made by DasoFabe

How many times do you want to repeat the process? 3
...

Message successfully sent to Discord.
Waiting for the next signup process...
```

## Customization

- You can customize the script to support different actions by modifying the `open_capcut_signup` function.
- To change the password or any other form field, locate the relevant line in the script and modify it.
  
## Troubleshooting

- **Selenium issues**: If you encounter issues with Selenium or WebDriver, ensure you have the correct version of ChromeDriver installed. You can also check the logs for any specific errors related to WebDriver or browser compatibility.
  
- **Verification code not found**: Ensure that the email is being received correctly in the temp-mail inbox. If the service is down or if there's a delay, the script may not find the email immediately.

## Disclaimer

This script is intended for educational purposes only. Automating the signup process on websites may violate their terms of service. Please ensure that you have permission from the service provider to automate such actions.
