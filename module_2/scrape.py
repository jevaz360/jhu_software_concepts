import json
import requests
from bs4 import BeautifulSoup

def gather_urls(url):
    urls = []
    pages = []
    for n in range(1,5):
        next_url = url + "&page=" + str(n)
        urls.append(next_url) 
        pages.append(n)
    return urls, pages

def make_entries(url):
    page = requests.get(url)

    # turn the contents of the page into a soup object
    soup = BeautifulSoup(page.content, "html.parser")

    # the blocks of entries start with the html tag <tr>, gather the entries on the page
    results_page = soup.find("div", class_= "tw-inline-block tw-min-w-full tw-py-2 tw-align-middle")
    results = results_page.find("tbody", class_="tw-divide-y tw-divide-gray-200 tw-bg-white")
    #print(results)

    entries = results.find_all("tr")
    return entries

def scrape(entries):
    #variables
    university = "None"
    program = "None"
    program_type_f = "None"
    entry_date_f = "None"
    decision_f = "None"
    href = "None"
    semester_start_f = "None"
    student_type_f = "None"
    gre_score_f = "None"
    gre_V_score_f = "None"
    gre_aw_score_f = "None"
    gpa_f = "None"
    comment_f = "None"
    home = "https://www.thegradcafe.com"
    count = 0
    list = []

    for entry in entries:
        if entry.find("td", class_ = "tw-py-5 tw-pr-3 tw-text-sm tw-pl-0") is not None:
            # when you reach the next entry, save the previous entry's data and store to json
            count+=1
            if count == 2:
                data = {
                "university": university,
                "program": program,
                "program_type":program_type_f,
                "entry date": entry_date_f,
                "decision": decision_f,
                "url_link": href,
                "start_semester": semester_start_f,
                "student_type": student_type_f,
                "GRE_score": gre_score_f,
                "GRE_V_score": gre_V_score_f,
                "GRE_AW_score": gre_aw_score_f,
                "GPA": gpa_f,
                "comment": comment_f
                }

                count = 1
                list.append(data)
    

            # university
            university_find = entry.find("div", class_= "tw-font-medium tw-text-gray-900 tw-text-sm")
            university = university_find.text
            #print(university)

            # program
            program_span = entry.find("span")
            program = program_span.text
            #print(program)

            # program type
            program_type = entry.find("span", class_ = "tw-text-gray-500")
            program_type_f = program_type.text
            #print(program_type.text)

            # date of entry
            entry_date = entry.find("td", class_ = "tw-px-3 tw-py-5 tw-text-sm tw-text-gray-500 tw-whitespace-nowrap tw-hidden md:tw-table-cell")
            entry_date_f = entry_date.text.strip()
            #print(entry_date.text.strip())

            # decision
            decision = entry.find("div", class_="tw-inline-flex tw-items-center tw-rounded-md tw-bg-red-50 tw-text-red-700 tw-ring-red-600/20 tw-px-2 tw-py-1 tw-text-sm tw-font-medium tw-ring-1 tw-ring-inset")
            if decision is not None:
                decision_f = decision.text.strip()    
                #print(decision.text.strip())
            else:
                decision = entry.find("div", class_ = "tw-inline-flex tw-items-center tw-rounded-md tw-bg-purple-50 tw-text-purple-700 tw-ring-purple-600/20 tw-px-2 tw-py-1 tw-text-sm tw-font-medium tw-ring-1 tw-ring-inset")
                if decision is not None:
                    decision_f = decision.text.strip()
                    #print(decision.text.strip())
                else:
                    decision = entry.find("div", class_="tw-inline-flex tw-items-center tw-rounded-md tw-bg-green-50 tw-text-green-700 tw-ring-green-600/20 tw-px-2 tw-py-1 tw-text-sm tw-font-medium tw-ring-1 tw-ring-inset")
                    if decision is not None:
                        decision_f = decision.text.strip()
                        #print(decision.text.strip())
                    else:
                        decision_f = "None"
                        #print("None")
            
            # URL link to entry
            more_tab = entry.find("a", class_="tw-block tw-px-3 tw-py-1 tw-text-sm tw-leading-6 tw-text-gray-900 tw-font-normal hover:tw-bg-gray-50")
            href = more_tab.get('href')
            href = home + href

            #print("Link: " + href)

        
        if entry.find("td", class_ = "tw-pt-2 tw-pb-5 tw-pr-4 tw-pl-0") is not None:
        
            # start semester
            semester_start = entry.find("div", class_ = "tw-inline-flex tw-items-center tw-rounded-md tw-bg-orange-400 tw-px-2 tw-py-1 tw-text-xs tw-font-medium tw-text-white tw-ring-1 tw-ring-inset tw-ring-orange-800/20")
            if semester_start.text is not None:
                semester_start_f = semester_start.text
                #print(semester_start.text)
            else:
                semester_start_f = "None"
                #print("None")

            # student type
            student_type = entry.find("div", class_= "tw-inline-flex tw-items-center tw-rounded-md tw-bg-stone-50 tw-px-2 tw-py-1 tw-text-xs tw-font-medium tw-text-stone-700 tw-ring-1 tw-ring-inset tw-ring-stone-600/20")
            student_type_f = student_type.text
            #print(student_type.text)

            # GRE_score
            gre_score = entry.find("div", string=lambda text: "gre" in text.lower())
            if gre_score is not None:
                gre_score_f = gre_score.text
                #print(gre_score.text)

            # GRE_V_score
            gre_V_score = entry.find("div", string=lambda text: "gre v" in text.lower())
            if gre_V_score is not None:
                gre_V_score_f = gre_V_score.text
                #print(gre_V_score.text)
            
            # GRE AW Score
            gre_aw_score = entry.find("div", string=lambda text:"gre aw" in text.lower())
            if gre_aw_score is not None:
                gre_aw_score_f = gre_aw_score.text
                #print(gre_aw_score.text)
            
            #GPA
            for n in range(5):  
                gpa = entry.find("div", string=lambda text:"gpa " + str(n) in text.lower())
                if gpa is not None:
                    gpa_f = gpa.text
                    #print(gpa.text)
            

        if entry.find("td", class_ = "tw-pb-5 tw-pr-4 sm:tw-pl-0 tw-pl-4") is not None:
            # comment
            comment = entry.find("p", class_= "tw-text-gray-500 tw-text-sm tw-my-0")
            comment_f = comment.text
            #print(comment.text)

    return list

def create_file():
        with open("data.json", "w") as json_file:
            return


def write_file(array):
    with open("data.json", "a") as json_file:
        json.dump(array, json_file, indent = 4)
    """
    for value in array:
        with open("data.json", "a") as json_file:
            json.dump(value, json_file, indent = 4)
    """



def main():
    # retrieve the url you want to scrape from
    url = "https://www.thegradcafe.com/survey/?q=Computer+Science"
    urls, pages = gather_urls(url)
    print(urls)
    print(pages)

    create_file()

    i=0
    array = []
    for url in urls:
        page = pages[i]
        entries = make_entries(url)

        list = scrape(entries)
        dictionary = {page:list}
        array.append(dictionary)
        #print(array)
        write_file(array)
        i+=1

main()