from bs4 import BeautifulSoup
import requests
import datetime as dt
import time

def find_jobs_day():
  today = dt.datetime.now()
  html_text = requests.get('https://glints.com/id/opportunities/jobs/explore?sortBy=latest&keywords=python&cities=28904').text
  soup = BeautifulSoup(html_text, 'lxml')

  jobs = soup.find_all('div' , class_ = 'JobCardsc__JobcardContainer-sc-1f9hdu8-0 RBKNv CompactOpportunityCardsc__CompactJobCardWrapper-sc-1xtox99-0 hFaCrl compact_job_card')

  for index, job in enumerate(jobs):
    posted_at = job.find('span', class_ = 'CompactOpportunityCardsc__UpdatedAtMessage-sc-1xtox99-16 dqeTyc').text[11:]
    if 'jam' in posted_at :
      job_title = job.find('h3', class_ ='CompactOpportunityCardsc__JobTitle-sc-1xtox99-7 kJpKeD').text
      company_name = job.find('a', class_ ='CompactOpportunityCardsc__CompanyLink-sc-1xtox99-8 bFxfxR').text
      job_location = job.find('p', class_ = 'CompactOpportunityCardsc__OpportunityInfo-sc-1xtox99-12 cgWCfq').text
      more_info = 'https://glints.com' + job.find('a', class_ ="CompactOpportunityCardsc__CardAnchorWrapper-sc-1xtox99-17 PRbbx job-search-results_job-card_link")['href']

      with open(f'job_posts/{today.strftime("%d %b %Y")}_{index}.txt', 'w') as f:
        f.write(f'''
        Job Title: {job_title}
        Company Name: {company_name}
        Location: {job_location}
        Posted At: {today.strftime("%a ,%d %b %Y")}
        URL Link: {more_info}

        ''')
        print('writing')


if __name__ == '__main__':
  counterback = 0
  while counterback < 1:
    find_jobs_day()
    counterback+=1
    # time_wait = 24*60
    # time.sleep(time_wait*60)
