import argparse
import csv
import time
from github import Github

#pip install PyGithub
#Start of function
def search_github(keywords):
    """Search for the keyword and save it to a csv file"""
    query = '+'.join(keywords) + '+in:readme+in:description'
    if args.ascending:
        result = g.search_repositories(query, order='asc', sort='stars')
    elif args.descending:
        result = g.search_repositories(query, order='desc', sort='stars')
    else:
        result = g.search_repositories(query)
    print(f'Found {result.totalCount} repo(s)')
    finalfilename = f"output-{str(timestamp_name())}.csv"
    with open(finalfilename, 'w+', newline='', encoding="utf-8") as csvFile:
        headwriter = csv.DictWriter(csvFile, fieldnames=["Project Name", "Description", "URL", "Programming Language",
                                                         "Last Updated"])
        headwriter.writeheader()
        writer = csv.writer(csvFile, delimiter=",")
        for repo in result:
            rate_limit = g.get_rate_limit()
            if rate_limit.search.remaining == 0:
                print('WARNING: Rate limit on searching was reached.  Results are incomplete.')
                break
            row = [str(repo.name), repo.description, repo.clone_url, str(repo.language), str(repo.updated_at)]
            writer.writerow(row)
    return True

def timestamp_name():
    """Updates the time and date for the csv filename"""
    timestr = time.strftime("%Y-%m-%d-%H-%M")
    return timestr

def main():
    """Main function of the program"""
    keywords = [keyword.strip() for keyword in search_term.split(',')]
    search_github(keywords)
    return True
#End of function

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('search_term', nargs='?', help="Input to search repository. To search with white space")
    parser.add_argument('account_token', nargs='?', help="Github username for authentication")
    parser.add_argument('-d', '--descending', action='store_true', help='Search result to descending order based on stars')
    parser.add_argument('-a', '--ascending', action='store_true', help='Search result to ascending order based on stars')
    args = parser.parse_args()
    search_term = args.search_term
    token = args.account_token
    g = Github(token)
    main()
