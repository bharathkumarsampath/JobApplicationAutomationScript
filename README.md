# Job Application Automation Script

This repository contains Python scripts designed to automate the job application process. The scripts allow users to apply for jobs by leveraging various configurations, prompts, and variables specific to the applying company and the user's work history.

## Features

- **Company-Specific Variables:** Customize job applications based on the specific company you are applying to.
- **User Work Experience Integration:** Easily integrate your work experience details into the job application process.
- **Prompt-Based Automation:** Generate customized job application content using prompts tailored to the role and company.

## Files Overview

1. **`applying_company_variables.py`**: 
   - Contains variables and configurations related to the company you are applying to.
   - Customize company-specific details such as company name, industry, and role requirements.

2. **`config.py`**: 
   - Configuration file that manages the overall settings and constants used across the scripts.
   - This file includes important configurations like API keys, directory paths, and other global settings.

3. **`prompt_job_applying.py`**:
   - This script generates customized prompts for job applications.
   - It uses the variables defined in the `applying_company_variables.py` and `worked_company_variables.py` files.

4. **`worked_company_variables.py`**:
   - Stores variables and details related to the user's previous work experience.
   - These details are used to customize job applications to highlight relevant experience.

## How to Use

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/job-application-automation.git
   cd job-application-automation
   ```

2. **Set Up Configurations:**

   - Edit the `config.py` file to add your specific configurations such as API keys and directory paths.

3. **Customize Company Variables:**

   - Modify the `applying_company_variables.py` and `worked_company_variables.py` files with details relevant to the company you are applying to and your work experience.

4. **Run the Scripts:**

   ```bash
   python prompt_job_applying.py
   ```

   - The script will generate job application content tailored to the company and role based on the provided variables.

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
