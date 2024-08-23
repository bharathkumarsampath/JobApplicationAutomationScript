import pyperclip
import argparse
import config
import applying_company_variables
import worked_company_variables
from datetime import date

# Setup argument parser
parser = argparse.ArgumentParser(description="Process a string and an integer argument.")
parser.add_argument('--prompt_type', type=str, default = "", help='a string argument')
parser.add_argument('--worked_role', type=str, default = "", help='a string argument')
parser.add_argument('--company', type=str, default = "", help='an integer argument')

# Parse the arguments
args = parser.parse_args()

def clean_string(s):
      lines = s.split('code_word_for_new_line')
      cleaned_lines = [' '.join(line.split()) for line in lines]
      return '\n\n'.join(cleaned_lines)


prompt = "do nothing"

if (args.prompt_type == "resume"):

      #company_index = args.company_index - 1

      company_index = worked_company_variables.company_to_index.get(args.company, 1)
      # Variables to be used inside the multiline string
      worked_role_name = args.worked_role
      worked_company = worked_company_variables.name_list[company_index - 1]
      worked_company_link = worked_company_variables.weblink_list[company_index - 1]
      worked_company_overview = worked_company_variables.overview_list[company_index - 1]


      prompt = f"""
            here is the website link : {applying_company_variables.weblink} for {applying_company_variables.name} and here is the website link for 
            {worked_company}:{worked_company_link}, go to the website link of each company and do your own research about both 
            {applying_company_variables.name} and {worked_company} code_word_for_new_line
            
            
            I worked in {worked_company} as a {worked_role_name}, code_word_for_new_line {worked_company_overview} code_word_for_new_line
            now am applying for the position {applying_company_variables.role_name} for the company {applying_company_variables.name}, 
            code_word_for_new_line {applying_company_variables.overview}code_word_for_new_line
            below is the job description : code_word_for_new_line {applying_company_variables.job_description} code_word_for_new_line

            
            now give me resume points, do not use headings as in resume, there supposed to be no headings and resume should have keywords 
            present in the job description which will help me in getting pass the ATS system, 
            the tools mentioned in the job description must be highlighted, but not in a artificial manner, 
            but in an organic manner of selling oneself, the length of each bullet point must be equal in 
            character count of 200 and should not be uneven, research about the company so that the bullet points 
            looks suitable for {worked_company} and also looks relevant to the job description I gave for {applying_company_variables.name}.
            code_word_for_new_line

            I want the employer to think I have used all of these tools in my previous experience at {worked_company}, so when you craft points, 
            I want you to do it in such a way that , you could employ these tools, make sure to use the art of story telling in our favor, 
            the story should be compelling and not boring for the employer, be as clear as sam altman , whoever is a clear thinker in history, 
            try to emulate them and think as clearly as possible and articulate in your thoughts and reasoning.code_word_for_new_line

            use star method, as employer like to see quantitative accomplishments and results and the situation in which the results are accomplished, 
            make sure the situation is specific to the {worked_company} domain area also relevant to {applying_company_variables.name} job description job duties 
            mentioned.code_word_for_new_line

            do not mention {applying_company_variables.name} name in the bullet points as the employer might think I tailored the resume for the job description 
            which will give myself away. 5 bullet points is enough. Using exact words in the job description might make people think I tailored the 
            resume to the job description.code_word_for_new_line
            
            Below are the skills highlighted by employer in the job description code_word_for_new_line : {applying_company_variables.required_skills} code_word_for_new_line 
            use these in explaining my achievements which will convince the employer, that I possess all the necessary skills for the job role
            """


      # Clean the multiline string
      multiline_string_cleaned = clean_string(prompt)

      # Copy to clipboard
      pyperclip.copy(multiline_string_cleaned)

      print("Resume Prompt copied to clipboard!")

elif(args.prompt_type == "skills" ):
      prompt = f"""for the job description below : code_word_for_new_line {applying_company_variables.job_description} code_word_for_new_line 
                   analyze and give me the important skills and tools that employer is expecting a potential candidate to have.code_word_for_new_line
                   give that in one line separated by comma, categorize skills into different categories"""
      
      multiline_string_cleaned = clean_string(prompt)

      # Copy to clipboard
      pyperclip.copy(multiline_string_cleaned)

      print("Skills Prompt copied to clipboard!")

elif(args.prompt_type == "coursework_undergrad"): 
      prompt = f"""choose coursework from undegrad : code_word_for_new_line {config.coursework_undergrad} code_word_for_new_line 
                   which are relevant to the job description below : code_word_for_new_line {applying_company_variables.job_description} code_word_for_new_line 
                   Adding relevant coursework to my resume for the job I am applying for will increase my chances of getting noticed by 
                   employers and being offered an interview. give me the result in one line separated by comma"""
      
      multiline_string_cleaned = clean_string(prompt)

      # Copy to clipboard
      pyperclip.copy(multiline_string_cleaned)

      print("Undergrad Coursework Prompt copied to clipboard!")


elif(args.prompt_type == "coursework_grad"): 
      prompt = f"""choose coursework from graduate degree : code_word_for_new_line {config.coursework_grad } code_word_for_new_line 
                   which are relevant to the job description below : code_word_for_new_line {applying_company_variables.job_description} code_word_for_new_line 
                   Adding relevant coursework to my resume for the job I am applying for will increase my chances of getting noticed by 
                   employers and being offered an interview. give me the result in one line separated by comma"""
      
      multiline_string_cleaned = clean_string(prompt)

      # Copy to clipboard
      pyperclip.copy(multiline_string_cleaned)

      print("Graduate Coursework Prompt copied to clipboard!")

elif(args.prompt_type == "resume_name"):
      # Get today's date
      today = date.today()

      # Format today's date as YYYYMMDD
      formatted_date = today.strftime("%Y%m%d")
      prompt = f"""BharathKumar_Sampath_{applying_company_variables.name.replace(" ", "_")}_{applying_company_variables.role_name.replace(" ", "_")}_{formatted_date}"""

      pyperclip.copy(prompt)

      print("name of the resume copied")

elif(args.prompt_type == "coverletter_name"):
      # Get today's date
      today = date.today()

      # Format today's date as YYYYMMDD
      formatted_date = today.strftime("%Y%m%d")
      prompt = f"""BharathKumar_Sampath_CoverLetter_{applying_company_variables.name.replace(" ", "_")}_{applying_company_variables.name.replace(" ", "_")}_{formatted_date}"""

      pyperclip.copy(prompt)

      print("name of the cover letter copied")

elif(args.prompt_type == "write_coverletter"):
     prompt = f"""write cover letter for the below job description :code_word_for_new_line {applying_company_variables.job_description} code_word_for_new_line
                  
                  am applying to {applying_company_variables.name} for the position {applying_company_variables.role_name}

                  make sure to highlight the skills below which was mentioned in the job description {applying_company_variables.required_skills}

                  I want you to tell things that are not present in the resume
                  """
      
     multiline_string_cleaned = clean_string(prompt)

      # Copy to clipboard
     pyperclip.copy(multiline_string_cleaned)

     print("Cover Letter Prompt copied to clipboard!") 
else:
      print("Did Nothing!") 
