from RssArticles_1 import posts

"""
This script is a continuation of the previous script, RssArticles_1.py.
It takes the list of dictionaries from the previous script and extracts only the titles and summaries of the articles.
It then combines the titles and summaries into a single string and returns a list of these strings.

Functions:
    OnlyTitlesandSummaries: Extracts only the titles and summaries from the list of dictionaries.
    TitleAndSummaryList: Combines the titles and summaries into a single string.
    PrintDeposit: Flattens the list of strings and returns it.

"""

def OnlyTitlesandSummaries():

    only_titles_and_summaries = []
    
    for x in posts:
        
        tempdict = {}
        
        try:
            tempdict["title"] = x["title"]
        except KeyError:
            tempdict["title"] = ""
        
        try:
            tempdict["summary"] = x["summary"]
        except KeyError:
            tempdict["summary"] = ""
        
        only_titles_and_summaries.append(tempdict)
    
    return only_titles_and_summaries

def TitleAndSummaryList(only_titles_and_summaries):

    title_and_summary_list = []
    
    for item in only_titles_and_summaries:
        
        combined = item["title"] + " " + item["summary"]
        
        title_and_summary_list.append([combined])
    
    return title_and_summary_list

def PrintDeposit(title_and_summary_list):
   
    flattened_list = []
    
    for item in title_and_summary_list:
        
        for value in item:
            
            flattened_list.append(value)
    
    return flattened_list


# The following code executes the functions above and prints the list of strings.

Only_the_titles_Summaries = OnlyTitlesandSummaries()
    
The_Title_Summary_List = TitleAndSummaryList(Only_the_titles_Summaries)
    
printdepositlist = PrintDeposit(The_Title_Summary_List)


# -------------------- MAIN EXECUTION SECTION --------------------

if __name__ == "__main__":
    print(printdepositlist)
