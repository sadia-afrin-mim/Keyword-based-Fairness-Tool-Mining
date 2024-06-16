from github import Github
from datetime import datetime, timedelta

def get_average_issue_resolve_time(repo_url, token):
    # Initialize GitHub object with access token
    g = Github(token)

    # Parse repository URL to extract owner and repo name
    owner, repo_name = repo_url.split('/')[-2:]

    # Get the repository object
    repo = g.get_repo(f"{owner}/{repo_name}")

    # Get all issues from the repository
    issues = repo.get_issues(state='closed')

    total_resolve_time = timedelta()
    total_issues = 0

    # Calculate total resolve time and total number of issues
    for issue in issues:
        if issue.closed_at is not None and issue.created_at is not None:
            resolve_time = issue.closed_at - issue.created_at
            total_resolve_time += resolve_time
            total_issues += 1

    # Calculate average resolve time
    if total_issues > 0:
        average_resolve_time = total_resolve_time / total_issues
        return average_resolve_time
    else:
        return timedelta(seconds=0)  # Return 0 if no closed issues found

if __name__ == "__main__":
    # Replace 'YOUR_GITHUB_TOKEN' with your actual GitHub token
    github_token = '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'

    # Replace 'OWNER/REPO_NAME' with the desired GitHub repository
    repository_url = 'https://github.com/Trusted-AI/AIF360'
    #https: // github.com / Trusted - AI / AIF360

    average_resolve_time = get_average_issue_resolve_time(repository_url, github_token)

    print(f"Average issue resolve time: {average_resolve_time}")